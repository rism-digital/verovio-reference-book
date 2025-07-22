---
title: "Other bindings"
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

### CocoaPods

You can use [CocoaPods](http://cocoapods.org/) to install `Verovio` by adding it to your to your `Podfile`:

```ruby
platform :ios, '16.0'
use_frameworks!
target 'MyApp' do
	pod 'Verovio', :git => 'https://github.com/rism-digital/verovio.git', :branch => 'master'
end
```

Then, run the following command:

```bash
pod install
```

To use Verovio in your iOS project import

```cpp
#import <Verovio/Verovio-umbrella.h>
```

See [https://github.com/Noroxs/VerovioExample](https://github.com/Noroxs/VerovioExample) for an example how to use it. To build and run the example, you need to:

* Navigate in the Terminal to the cloned directory
* Execute pod update
* Open the VerovioExample.xcworkspace and NOT the VerovioExample.xcodeproj
* Build and Run on any simulator or device
