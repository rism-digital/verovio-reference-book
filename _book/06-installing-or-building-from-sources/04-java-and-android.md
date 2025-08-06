---
title: "Java and Android"
---

### Java

To build the Java toolkit you need to have swig and swig-java installed on your machine (see <a href="http://swig.org" target="_blank">SWIG</a>) as well as [Maven](https://maven.apache.org/). You need to run:

```bash
cd bindings/java
mvn package
mvn package
```

Note the `mvn package` command needs to be run twice. You can test it with the MEI and PAE examples. For example – replace `X.X.X` with the appropriate version number:

```bash
cd example-mei
javac -cp .:../target/VerovioToolkit-X.X.X.jar main.java 
java -cp .:../target/VerovioToolkit-X.X.X.jar main
```

This should write an `output.svg` file in the current directory. The PAE example will write the SVG to the standard output.

See [this](https://github.com/rism-ch/verovio/issues/996) issue for SVG output problems on non US Ubuntu installations.

### Android

The simplest way to use Verovio in Android is to use the Java bindings provided by Verovio. You can have it generated and compiled directly in Android Studio. The [sample application repository](https://github.com/rism-digital/verovio-android-demo) provides a complete example on how to use it, with Verovio included as a submodule in `external/verovio`. You need swig to be installed on your machine.

The `app/build.gradle.kts` includes a step to generate the swig binding for Java and to build the toolkit:

```
////////////////////////////////////////////
// Generate the java and cpp files using swig and write them into the project
val swigOutputJava = file("src/main/java/org/verovio/lib")
val swigOutputCpp = file("src/main/cpp/verovio_wrap.cxx")
val swigInterfaceFile = file("${rootDir.absolutePath}/external/verovio/bindings/java/verovio.i")

tasks.register<Exec>("generateSwigBindings") {
    group = "build"
    description = "Generate JNI bindings with SWIG"

    // Adjust working directory to the project root
    workingDir = rootProject.projectDir

    // Ensure output directories exist
    doFirst {
        swigOutputJava.mkdirs()
        swigOutputCpp.parentFile.mkdirs()
    }

    commandLine = listOf(
        "/opt/homebrew/bin/swig", // Change to "/bin/swig" or something else if needed
        "-java",
        "-c++",
        "-package", "org.verovio.lib",
        "-outdir", swigOutputJava.absolutePath,
        "-o", swigOutputCpp.absolutePath,
        swigInterfaceFile.absolutePath
    )
}

// Ensure SWIG runs before compilation
tasks.named("preBuild") {
    dependsOn("generateSwigBindings")
}

tasks.named("clean") {
    doFirst {
        delete("src/main/java/org/verovio/lib/*")
        delete("src/main/cpp/verovio_wrap.cxx")
    }
}
```

The file also includes a step to copy the resource directory:

```
////////////////////////////////////////////
// Copy the verovio resource directory from the submodule to the project
tasks.register<Copy>("copyVerovioData") {
    from(rootDir.resolve("external/verovio/data"))
    into("src/main/assets/verovio/data")
}

tasks.named("preBuild") {
    dependsOn("copyVerovioData")
}
```