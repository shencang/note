# java

## 未分类

[Java图像化awt，swing，SWT的联系和区别](https://github.com/shencang/note/tree/master/Java/Java图像化awt，swing，SWT的联系和区别.md)

### JAVA - String 中删除指定字符（11种方法）

* 第一种方法

通过循环从前往后遍历，如果不是要删除的字符则加到处理后的字符串中，代码如下：

```java
    public String deleteCharString0(String sourceString, char chElemData) {
        String deleteString = "";
        for (int i = 0; i < sourceString.length(); i++) {
            if (sourceString.charAt(i) != chElemData) {
                deleteString += sourceString.charAt(i);
            }
        }
        return deleteString;
    }
```

* 第二种方法

通过循环确定要删除字符的位置索引，然后通过分割字符串的形式，将子字符串拼接，注意最后一段子字符串和源字符串中没有要删除字符的情况，代码如下：

```java
    public String deleteCharString1(String sourceString, char chElemData) {
        String deleteString = "";
        int iIndex = 0;
        for (int i = 0; i < sourceString.length(); i++) {
            if (sourceString.charAt(i) == chElemData) {
                if (i > 0) {
                    deleteString += sourceString.substring(iIndex, i);
                }
                iIndex = i + 1;
            }
        }
        if (iIndex <= sourceString.length()) {
            deleteString += sourceString.substring(iIndex, sourceString.length());
        }
        return deleteString;
    }
```

* 第三种方法

原理同上，只不过查找要删除字符位置采用String类中的函数执行，效率不如上面的高，代码如下：

```java
    public String deleteCharString2(String sourceString, char chElemData) {
        String deleteString = "";
        int iIndex = 0;
        int tmpCount = 0;
        do {
            tmpCount = sourceString.indexOf(chElemData, iIndex);
            if (tmpCount > 0) {
                deleteString += sourceString.substring(iIndex, tmpCount);
            }
            if (tmpCount != -1) {
                iIndex = tmpCount + 1;
            }
        } while (tmpCount != -1);
        if (iIndex <= sourceString.length()) {
            deleteString += sourceString.substring(iIndex, sourceString.length());
        }
        return deleteString;
    }
```

* 第四种方法

原理与上方基本一致，只不过这次采用倒序方式，这里的坑就更多了，一定要注意索引的取值范围和是否合法，代码如下：

```java
    public String deleteCharString3(String sourceString, char chElemData) {
        String deleteString = "";
        int iIndex = sourceString.length();
        int tmpCount = 0;
        do {
            tmpCount = sourceString.lastIndexOf(chElemData, iIndex - 1);
            if (tmpCount < sourceString.length() && tmpCount >= 0) {
                deleteString = sourceString.substring(tmpCount + 1, iIndex) + deleteString;
            }
            if (tmpCount != -1) {
                iIndex = tmpCount;
            }
        } while (tmpCount != -1);
        if (iIndex >= 0) {
            deleteString = sourceString.substring(0, iIndex) + deleteString;
        }

        return deleteString;
    }

```

* 第五种方法

通过采用正则的方式和replaceAll函数，本种方法要注意特殊字符，例如正则中的 “.”字符，需要对特殊字符进行转义，代码如下：

```java
    public String deleteCharString4(String sourceString, char chElemData) {
        String deleteString = "";
        final String strTable = "|^$*+?.(){}\\";
        String tmpRegex = "[";
        for (int i = 0; i < strTable.length(); i++) {
            if (strTable.charAt(i) == chElemData) {
                tmpRegex += "\\";
                break;
            }
        }
        tmpRegex += chElemData + "]";
        deleteString = sourceString.replaceAll(tmpRegex, "");
        return deleteString;
    }

```

* 第六种方法

采用正则的方式将字符串分割成几个子字符串，再将子字符串进行拼接，代码如下：

```java
    public String deleteCharString5(String sourceString, char chElemData) {
        String deleteString = "";
        final String strTable = "|^$*+?.(){}\\";
        String tmpRegex = "[";
        for (int i = 0; i < strTable.length(); i++) {
            if (strTable.charAt(i) == chElemData) {
                tmpRegex += "\\";
                break;
            }
        }
        tmpRegex += chElemData + "]";
        String[] tmpStringArray = sourceString.split(tmpRegex);
        for (int i = 0; i < tmpStringArray.length; i++) {
            deleteString += tmpStringArray[i];
        }
        return deleteString;
    }

```

* 第七种方法

将字符编程可读序列，在通过 String 类中的方法替换，代码如下：

```java
    public String deleteCharString6(String sourceString, char chElemData) {
        String tmpString = "";
        tmpString += chElemData;
        tmpString.subSequence(0, 0);
        String deleteString = "";
        deleteString = sourceString.replace(tmpString, deleteString.subSequence(0, 0));
        return deleteString;
    }

```

* 第八种方法

把原字符串转化为字符数组，然后原理与直接插入排序原理类似，代码如下：

```java
    public String deleteCharString7(String sourceString, char chElemData) {
        String deleteString = "";
        char[] Bytes = sourceString.toCharArray();
        int iSize = Bytes.length;
        for (int i = Bytes.length - 1; i >= 0; i--) {
            if (Bytes[i] == chElemData) {
                for (int j = i; j < iSize - 1; j++) {
                    Bytes[j] = Bytes[j + 1];
                }
                iSize--;
            }
        }
        for (int i = 0; i < iSize; i++) {
            deleteString += Bytes[i];
        }
        return deleteString;
    }
```

* 第九种方法

原理与 第一种方法 类似，本次采用 stringBuffer 类中的 append 方法进行操作，我认为效率应该高于第一种。

```java
    public String deleteCharString8(String sourceString, char chElemData) {
        StringBuffer stringBuffer = new StringBuffer("");
        for (int i = 0; i < sourceString.length(); i++) {
            if (sourceString.charAt(i) != chElemData) {
                stringBuffer.append(sourceString.charAt(i));
            }
        }
        return stringBuffer.toString();
    }
```

* 第十种方法

采用 stringBuffer 类中的 replace and indexOf 方法（_ 故意凑方法），代码如下：

```java
    public String deleteCharString9(String sourceString, char chElemData) {
        String tmpString = "";
        tmpString += chElemData;
        StringBuffer stringBuffer = new StringBuffer(sourceString);
        int iFlag = -1;
        do {
            iFlag = stringBuffer.indexOf(tmpString);
            if (iFlag != -1) {
                stringBuffer = stringBuffer.replace(iFlag, iFlag + 1, "");
            }
        } while (iFlag != -1);
        return stringBuffer.toString();
    }
```

* 第十一种方法

采用 stringBuffer 类中的 deleteCharAt 和 indexOf 直接删除

```java
    public String deleteCharString10(String sourceString, char chElemData) {
        String tmpString = "";
        tmpString += chElemData;
        StringBuffer stringBuffer = new StringBuffer(sourceString);
        int iFlag = -1;
        do {
            iFlag = stringBuffer.indexOf(tmpString);
            if (iFlag != -1) {
                stringBuffer.deleteCharAt(iFlag);
            }
        } while (iFlag != -1);
        return stringBuffer.toString();
    }
```
