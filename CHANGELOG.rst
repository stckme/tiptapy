=======
History
=======

0.20.0 (2024-06-14)
-------------------
- Underline mark added.

0.19.0 (2024-06-06)
-------------------
- Render attrs for parent tag in block if present, only rendering `id` for now.

0.18.1 (2024-02-21)
-------------------
- Fixed blocks data getting updated due to pass by reference

0.18.0 (2024-02-09)
-------------------
- html.escape all the attributes
- Match link domain more precisely
- Image height or width can be individually specified

0.16.0 (2023-03-14)
-------------------
* Support for new tiptap versions that uses camelCase over snake_case

0.15.0 (2022-07-27)
-------------------
* A few fixes and more Jinja based conversion

0.14.0 (2022-07-18)
-------------------
* Escape markup while converting to HTML

0.13.2 (2022-01-07)
-------------------
* New Doc attribute `locked` to support guest views
* Doc.templates_path is now immutable 

0.13.0 (2021-12-27)
-------------------
* Major rewrite that moved rendering logic to jinja templates (no longer python string manipulations)

0.12.0 (2021-11-23)
-------------------
* Start attribute added for Ordered List

0.11.1 (2021-06-30)
-------------------
* Style changes for Documents

0.11.0 (2021-05-25)
-------------------
* Image width height support

0.10.0 (2021-01-02)
-------------------
* Document block support

0.9.0 (2020-12-02)
------------------
* Code block support

0.8.0 (2020-09-23)
------------------
* Audio block support

0.7.7 (2020-08-10)
------------------
* Paragraph rendering fix

0.7.6 (2020-07-24)
------------------
* Support for superscript

0.7.5 (2020-07-24)
------------------
* Standardized anchor tag for known and unknown providers
* Updated `Image` and `FeatureImage` to support updated image JSON structure.
* Rendered HTML of `Image` and `FeatureImage` have MIME type of supported image extensions.
* Added Deepsource as code quality tool.
* Code simplification
* HTML fixes

0.7.0 (2020-07-06)
------------------
* Corrected Heading node to be a container type
* Added long pending HTML escaping

0.6.8 (2020-07-03)
------------------
* `is_renderable` is made mandatory in render function to validate JSON data.

0.6.7 (2020-07-02)
------------------
* Added optional `is_renderable` function in the base node.

0.6.6 (2020-06-11)
------------------
* Improved Heading Block to accept nested text content 

0.6.5 (2020-06-09)
------------------
* Heading block added

0.6.4 (2020-06-08)
------------------
* Improved Embed block rendered html output.

0.6.3 (2020-04-24)
------------------
* Media tags tests improved

0.6.0 (2020-04-24)
------------------
* New node: Embed
* Docstrings for base classes
* Simplified testing
* Bumpversion support added for easier release process

0.5.0 (2020-04-16)
------------------
* Added extras module to support non upstream (tiptap) supported blocks

0.4.1 (2020-03-27)
------------------
* Supported ordered lists

0.4.0 (2020-01-17)
------------------

* Added tests
* Travis CI setup 
* Supported a few tags

0.3.0 (2020-01-17)
------------------

* Added support for link mark and mark atrributes
* Added BlockQuote and Hardbreak
* Used Black formatter
