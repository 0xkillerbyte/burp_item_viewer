# BIV = Burp Items Viewer
Simple Python scripts that creates an HTML page report that contains all http proxy saved items. The free burpsuite version permits to save the items but not permits to reopen theme; BIV solve this problem.
## How to use:
- Save the desidered items from Proxy-> HTTP History, then select "Save Items" by click right mouse button.
- Select "Base64-encode requests and responses" and save the file with xml extension.
- Then run: 
```
python burp_report.py ../../Desktop/myitems.xml
``` 
- Open the myitems.xml.html file with your favourite browser to explore the report.

![screenshot](https://image.ibb.co/mMMapm/Screenshot_from_2017_12_24_18_45_58.png)

## Changelog:
- Release 0.0.0.1alpha:
    - Shows Request, Response and Response Rendering
    - Sorting for each column