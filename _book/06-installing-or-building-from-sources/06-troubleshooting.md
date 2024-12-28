---
title: "Troubleshooting"
---

This page contains descriptions and potential fixes for common issues when installing Verovio from source. 

### C-Compiler error on macOS

When trying to build Verovio from the sources and you've updated the system and the repository, but the CMake file was created a while ago, it might have gone out-of-sync and needs to be regenerated. You might see an error message like:

```bash
-- The C compiler identification is AppleClang 14.0.0.14000029
-- The CXX compiler identification is AppleClang 14.0.0.14000029
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - failed
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - broken
CMake Error at /usr/local/Cellar/cmake/3.25.1/share/cmake/Modules/CMakeTestCCompiler.cmake:70 (message):
  The C compiler

    "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc"

  is not able to compile a simple test program.
```

#### Solution

Rerun cmake with the `--fresh` option (CMake 3.24 and later) or simply delete the `tools/CMakeFiles` directory before [installing it from sources](/installing-or-building-from-sources/command-line.html).
