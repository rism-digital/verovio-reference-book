**Selection parameter**

The JSON object can have a `measureRange`, a `start` and `end`, or can be empty for re-setting the selection. The measure range in `measureRange` is 1-based. The position value is the index position of the measure and not the `measure@n` value. The values `start` and `end` can be used as range to specify the beginning and respectively the end of the document. When specifying `start` or `end` keys, the values must refer to the `measure@xml:id`.

Examples of parameters:
```json
{ "measureRange": "2-3" }
{ "measureRange": "82-end" }
{ "measureRange": "38" }
{ "start": "measure-L337", "end": "measure-L355" }
{}
```
