---
title: "Swift and Objective-C"
---

### Swift

The Swift binding of Verovio can easily be install with the Swift Package Manager. In xcode, this can be done with adding a package dependency (e.g., through **File > Add Package Dependency...**) and by providing the Verovio GitHub repository. You might need to add an empty `Bridging-Header.h` file to your project.

Once this is done, Verovio is available in Swift with:

```swift
import VerovioToolkit

var toolkit = VerovioToolkit()
```

Note that the constructor in the Swift binding does not set the resource path. You need to do it explicitly by calling `toolkit.setResourcePath`. The nice thing, however, is that the Swift binding provides a `VerovioResources.bundle` with the Verovio resources. So setting the resources will look like:

```swift
let bundle = VerovioResources.bundle

if let resourceURL = bundle.url(forResource: "data", withExtension: nil) {
    let resourcePath = resourceURL.deletingLastPathComponent().path
    let _ = toolkit.setResourcePath(resourcePath + "/data")
} else {
    print("Could not find resource URL for 'data'")
}
```

Loading some data and rendering will work with the usual methods of the toolkit:
```swift
let res = toolkit.loadData(data)
let svg = toolkit.renderToSVG(1, false)
```

### Objective-C with CocoaPods

The simplest way to use Verovio in Objective-C is to use [CocoaPods](http://cocoapods.org/) to install `Verovio` by adding it to your to your `Podfile`:

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

Then you can create an Objective-C wrapper with the following `VerovioToolkitWrapper.h/mm` files (here with a few sample methods):

```objective-c
#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface VerovioToolkitWrapper : NSObject

- (instancetype)init;
- (NSInteger)getPageCount;
- (NSString *)getVersion;
- (BOOL)loadData:(NSString *)data;
- (void)redoLayout;
- (NSString *)renderToSVG:(NSInteger)pageNo;
- (void)setOptions:(nullable NSString *)jsonOptions;

@end

NS_ASSUME_NONNULL_END
```

```objective-c
#import "VerovioToolkitWrapper.h"

// Include the umbrella header
#import <Verovio/Verovio-umbrella.h>

// Include the C++ Verovio header
#include <verovio/toolkit.h>


@implementation VerovioToolkitWrapper {
    std::unique_ptr<vrv::Toolkit> toolkit;
}

- (instancetype)init {
    self = [super init];
    if (self) {
        NSBundle *verovioBundle = [NSBundle bundleWithIdentifier:@"digital.rism.VerovioFramework"];
        //NSLog(@"Bundle path: %@", verovioBundle.bundlePath);
        NSString *resourcePath = [verovioBundle URLsForResourcesWithExtension:@"xml"
            subdirectory:@"data"]
            .firstObject.URLByDeletingLastPathComponent.path;

        // Obviously it would be good to check that verovioBundle and resourcePath are not nil
        toolkit = std::make_unique<vrv::Toolkit>(false);
        toolkit->SetResourcePath([resourcePath cStringUsingEncoding:NSUTF8StringEncoding]);
    }
    return self;
}

- (NSInteger)getPageCount {
    return toolkit->GetPageCount();
}

- (NSString *)getVersion {
    std::string version = toolkit->GetVersion();
    return [NSString stringWithUTF8String:version.c_str()];
}

- (BOOL)loadData:(NSString *)data {
    std::string input = [data UTF8String];
    return toolkit->LoadData(input);
}

- (NSString *)renderToSVG:(NSInteger)pageNo {
    std::string svg = toolkit->RenderToSVG((int)pageNo);
    return [NSString stringWithUTF8String:svg.c_str()];
}

- (void)redoLayout {
    toolkit->RedoLayout();
}

- (void)setOptions:(nullable NSString *)jsonOptions {
    std::string options = jsonOptions ? [jsonOptions UTF8String] : "";
    toolkit->SetOptions(options);
}

@end
```