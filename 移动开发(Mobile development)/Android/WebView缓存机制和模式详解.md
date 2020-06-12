# WebView 缓存机制和模式详解

```T
 当我们加载Html时候，会在我们data/应用package下生成database与cache两个文件夹:
我们请求的Url记录是保存在webviewCache.db里，而url的内容是保存在webviewCache文件夹下.
WebView中存在着两种缓存：网页数据缓存（存储打开过的页面及资源）、H5缓存（即AppCache）。

```

## 一、网页缓存

### 1、缓存构成

```t
/data/data/package_name/cache/
/data/data/package_name/database/webview.db
/data/data/package_name/database/webviewCache.db
```

```t
综合可以得知 webview 会将我们浏览过的网页url已经网页文件(css、图片、js等)保存到数据库表中
```

``缓存模式(5种)``

* LOAD_CACHE_ONLY:  不使用网络，只读取本地缓存数据

* LOAD_DEFAULT:  根据cache-control决定是否从网络上取数据。

* LOAD_CACHE_NORMAL: API level 17中已经废弃, 从API level 11开始作用同LOAD_DEFAULT模式

* LOAD_NO_CACHE: 不使用缓存，只从网络获取数据.

* LOAD_CACHE_ELSE_NETWORK，只要本地有，无论是否过期，或者no-cache，都使用缓存中的数据。

```t
如：www.taobao.com的cache-control为no-cache，在模式LOAD_DEFAULT下，无论如何都会从网络上取数据，如果没有网络，就会出现错误页面；在LOAD_CACHE_ELSE_NETWORK模式下，无论是否有网络，只要本地有缓存，都使用缓存。本地没有缓存时才从网络上获取。
www.360.com.cn的cache-control为max-age=60，在两种模式下都使用本地缓存数据。
```

* 总结：根据以上两种模式，建议缓存策略为，判断是否有网络，有的话，使用LOAD_DEFAULT，无网络时，使用LOAD_CACHE_ELSE_NETWORK。

``设置WebView 缓存模式``

```java
    private void initWebView() {  

            mWebView.getSettings().setJavaScriptEnabled(true);  
            mWebView.getSettings().setRenderPriority(RenderPriority.HIGH);  
            mWebView.getSettings().setCacheMode(WebSettings.LOAD_DEFAULT);  //设置 缓存模式  
            // 开启 DOM storage API 功能  
            mWebView.getSettings().setDomStorageEnabled(true);  
            //开启 database storage API 功能  
            mWebView.getSettings().setDatabaseEnabled(true);
            String cacheDirPath = getFilesDir().getAbsolutePath()+APP_CACAHE_DIRNAME;  
    //      String cacheDirPath = getCacheDir().getAbsolutePath()+Constant.APP_DB_DIRNAME;  
            Log.i(TAG, "cacheDirPath="+cacheDirPath);  
            //设置数据库缓存路径  
            mWebView.getSettings().setDatabasePath(cacheDirPath);  
            //设置  Application Caches 缓存目录  
            mWebView.getSettings().setAppCachePath(cacheDirPath);  
            //开启 Application Caches 功能  
            mWebView.getSettings().setAppCacheEnabled(true);  
        }
```

``清除缓存``

```java
    /**
         * 清除WebView缓存
         */  
        public void clearWebViewCache(){  

            //清理Webview缓存数据库  
            try {  
                deleteDatabase("webview.db");
                deleteDatabase("webviewCache.db");  
            } catch (Exception e) {  
                e.printStackTrace();  
            }  

            //WebView 缓存文件  
            File appCacheDir = new File(getFilesDir().getAbsolutePath()+APP_CACAHE_DIRNAME);  
            Log.e(TAG, "appCacheDir path="+appCacheDir.getAbsolutePath());  

            File webviewCacheDir = new File(getCacheDir().getAbsolutePath()+"/webviewCache");  
            Log.e(TAG, "webviewCacheDir path="+webviewCacheDir.getAbsolutePath());  

            //删除webview 缓存目录  
            if(webviewCacheDir.exists()){  
                deleteFile(webviewCacheDir);  
            }  
            //删除webview 缓存 缓存目录  
            if(appCacheDir.exists()){  
                deleteFile(appCacheDir);  
            }  
        }
```

``完整代码``

```java
package com.example.webviewtest;  
  
import java.io.File;  
  
import android.app.Activity;  
import android.graphics.Bitmap;  
import android.os.Bundle;  
import android.util.Log;  
import android.view.View;  
import android.webkit.JsPromptResult;  
import android.webkit.JsResult;  
import android.webkit.WebChromeClient;  
import android.webkit.WebSettings;  
import android.webkit.WebSettings.RenderPriority;  
import android.webkit.WebView;  
import android.webkit.WebViewClient;  
import android.widget.RelativeLayout;  
import android.widget.TextView;  
import android.widget.Toast;  
  
public class MainActivity extends Activity {  
  
    private static final String TAG = MainActivity.class.getSimpleName();  
    private static final String APP_CACAHE_DIRNAME = "/webcache";  
    private TextView tv_topbar_title;  
    private RelativeLayout rl_loading;  
    private WebView mWebView;  
    private String url;  
  
    @Override  
    protected void onCreate(Bundle savedInstanceState) {  
        super.onCreate(savedInstanceState);  
        setContentView(R.layout.activity_main);  

        //url:http://m.dianhua.cn/detail/31ccb426119d3c9eaa794df686c58636121d38bc?apikey=jFaWGVHdFVhekZYWTBWV1ZHSkZOVlJWY&app=com.yulore.yellowsdk_ios&uid=355136051337627  
        url = "http://m.dianhua.cn/detail/31ccb426119d3c9eaa794df686c58636121d38bc?apikey=jFaWGVHdFVhekZYWTBWV1ZHSkZOVlJWY&app=com.yulore.yellowsdk_ios&uid=355136051337627";  
        findView();  
    }  
  
    private void findView() {  

        tv_topbar_title = (TextView) findViewById(R.id.tv_topbar_title);  

        rl_loading = (RelativeLayout) findViewById(R.id.rl_loading);  

        mWebView = (WebView) findViewById(R.id.mWebView);  

        initWebView();  

        mWebView.setWebViewClient(new WebViewClient() {  
  
            @Override  
            public void onLoadResource(WebView view, String url) {  

                Log.i(TAG, "onLoadResource url="+url);  

                super.onLoadResource(view, url);  
            }  
  
            @Override  
            public boolean shouldOverrideUrlLoading(WebView webview, String url) {  
  
                Log.i(TAG, "intercept url="+url);  

                webview.loadUrl(url);  
  
                return true;  
            }  
  
            @Override  
            public void onPageStarted(WebView view, String url, Bitmap favicon) {  

                Log.e(TAG, "onPageStarted");  

                rl_loading.setVisibility(View.VISIBLE); // 显示加载界面  
            }  
  
            @Override  
            public void onPageFinished(WebView view, String url) {  
  
                String title = view.getTitle();  
  
                Log.e(TAG, "onPageFinished WebView title=" + title);  
  
                tv_topbar_title.setText(title);  
                tv_topbar_title.setVisibility(View.VISIBLE);  
  
                rl_loading.setVisibility(View.GONE); // 隐藏加载界面  
            }  
  
            @Override  
            public void onReceivedError(WebView view, int errorCode, String description, String failingUrl) {  
  
                rl_loading.setVisibility(View.GONE); // 隐藏加载界面  
  
                Toast.makeText(getApplicationContext(), "",  
                        Toast.LENGTH_LONG).show();  
            }  
        });  
  
        mWebView.setWebChromeClient(new WebChromeClient() {  
  
            @Override  
            public boolean onJsAlert(WebView view, String url, String message, JsResult result) {  
  
                Log.e(TAG, "onJsAlert " + message);  
  
                Toast.makeText(getApplicationContext(), message, Toast.LENGTH_SHORT).show();  
  
                result.confirm();  
  
                return true;  
            }  
  
            @Override  
            public boolean onJsConfirm(WebView view, String url, String message, JsResult result) {  
  
                Log.e(TAG, "onJsConfirm " + message);  
  
                return super.onJsConfirm(view, url, message, result);  
            }  
  
            @Override  
            public boolean onJsPrompt(WebView view, String url, String message, String defaultValue, JsPromptResult result) {  
  
                Log.e(TAG, "onJsPrompt " + url);  
  
                return super.onJsPrompt(view, url, message, defaultValue, result);  
            }  
        });  

        mWebView.loadUrl(url);  
    }  
  
    private void initWebView() {  

        mWebView.getSettings().setJavaScriptEnabled(true);  
        mWebView.getSettings().setRenderPriority(RenderPriority.HIGH);  
        mWebView.getSettings().setCacheMode(WebSettings.LOAD_DEFAULT);  //设置 缓存模式  
        // 开启 DOM storage API 功能  
        mWebView.getSettings().setDomStorageEnabled(true);  
        //开启 database storage API 功能  
        mWebView.getSettings().setDatabaseEnabled(true);
        String cacheDirPath = getFilesDir().getAbsolutePath()+APP_CACAHE_DIRNAME;  
//      String cacheDirPath = getCacheDir().getAbsolutePath()+Constant.APP_DB_DIRNAME;  
        Log.i(TAG, "cacheDirPath="+cacheDirPath);  
        //设置数据库缓存路径  
        mWebView.getSettings().setDatabasePath(cacheDirPath);  
        //设置  Application Caches 缓存目录  
        mWebView.getSettings().setAppCachePath(cacheDirPath);  
        //开启 Application Caches 功能  
        mWebView.getSettings().setAppCacheEnabled(true);  
    }  

    /**
     * 清除WebView缓存
     */  
    public void clearWebViewCache(){  

        //清理Webview缓存数据库  
        try {  
            deleteDatabase("webview.db");
            deleteDatabase("webviewCache.db");  
        } catch (Exception e) {  
            e.printStackTrace();  
        }  

        //WebView 缓存文件  
        File appCacheDir = new File(getFilesDir().getAbsolutePath()+APP_CACAHE_DIRNAME);  
        Log.e(TAG, "appCacheDir path="+appCacheDir.getAbsolutePath());  

        File webviewCacheDir = new File(getCacheDir().getAbsolutePath()+"/webviewCache");  
        Log.e(TAG, "webviewCacheDir path="+webviewCacheDir.getAbsolutePath());  

        //删除webview 缓存目录  
        if(webviewCacheDir.exists()){  
            deleteFile(webviewCacheDir);  
        }  
        //删除webview 缓存 缓存目录  
        if(appCacheDir.exists()){  
            deleteFile(appCacheDir);  
        }  
    }  

    /**
     * 递归删除 文件/文件夹
     *  
     * @param file
     */  
    public void deleteFile(File file) {  
  
        Log.i(TAG, "delete file path=" + file.getAbsolutePath());  

        if (file.exists()) {  
            if (file.isFile()) {  
                file.delete();  
            } else if (file.isDirectory()) {  
                File files[] = file.listFiles();  
                for (int i = 0; i < files.length; i++) {  
                    deleteFile(files[i]);  
                }  
            }  
            file.delete();  
        } else {  
            Log.e(TAG, "delete file no exists " + file.getAbsolutePath());  
        }  
    }  
  
}
```
