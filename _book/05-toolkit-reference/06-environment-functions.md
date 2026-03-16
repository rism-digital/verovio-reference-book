---
title: "Environment functions"
---

Verovio includes a few environment-level functions for configuring the global setup in which the toolkit runs. They are namespace-level functions in the C++ codebase. For the Python and JavaScript bindings, they are module-level functions.

### SetDefaultResourcePath

Specify the path where the resources are located.

{% aside .warning %}This method is not available in the JavaScript distributed version of the toolkit{% endaside %}

**Returns**

`void`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `path` | `const std::string &` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
void vrv::SetDefaultResourcePath(const std::string &path)
```

**Example call**

```python
verovio.setDefaultResourcePath(path)
```

### EnableLog

**Returns**

`void`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `level` | `LogLevel` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
void vrv::EnableLog(LogLevel level);
```

**Example call**

```python
verovio.enableLog(level)
```

**LogLevel**

The `LogLevel` enum includes the following values:
* `LOG_OFF`: no log
* `LOG_DEBUG`: log all messages, including debug ones
* `LOG_INFO`: log all messages
* `LOG_WARNING`: log error and warning messages (default)
* `LOG_ERROR`: log error messages only

For both the Python and the JavaScript bindings, the values are available in the modules. This means that the log level can be changed with:

```python
import verovio
verovio.enableLog(verovio.LOG_ERROR)
```

```html
<script>
  document.addEventListener("DOMContentLoaded", (event) => {
      verovio.module.onRuntimeInitialized = () => {
        verovio.enableLog(verovio.LOG_ERROR);
      }
  });
</script>
```

### EnableLogToBuffer

Redirect the log messages to a buffer instead of the `std::err` or the console. The messages can be accessed from the toolkit instance via the `GetLog()` method.

**Returns**

`void`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `value` | `bool` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
void vrv::EnableLogToBuffer(bool value);
```

**Example call**

```python
verovio.enableLogToBuffer(value)
```
