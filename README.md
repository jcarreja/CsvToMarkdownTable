# CSV To Markdown Table

Simple Python 2.7 CSV to Markdown Table Converter

Requires **no external libraries**.

Has been completely inspired and adapted from the Javascript version [donatj/CsvToMarkdownTable](https://github.com/donatj/CsvToMarkdownTable).

Example Use:

```python
python csv_to_markdown.py example_csv_file.csv --delimiter , --hasHeader
python markdown_to_csv.py example_md_file.md
```

Outputs:

```
| header1 | header2 | header3 |
|---------|---------|---------|
| Value1  | Value2  | Value3  |
```

Which displays in markdown as:

| header1 | header2 | header3 |
|---------|---------|---------|
| Value1  | Value2  | Value3  |
