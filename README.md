# lilac_timer
紫丁香辩论赛计时器



# 直接使用

在有Img和Msc文件的目录运行exe。
在设计页面输入各项内容，设置时间项目，点击“开始计时”按钮跳转至计时页面。
在计时页面点击实现跳转页面或开始计时或切换计时，在计时开始后，不能通过点击页面跳转。
下方菜单按钮实现异步跳转以及退出。

# 开发手册

## 安装依赖

```bash
pip install -r requirements
```

## 运行

```bash
python app.py
```

## 更新ui

### 自动构建

在设置DEBUG模式，每次运行app会自动构建

### 手动构建

```bash
python tools.py
```

## 打包为exe

```bash
python release.py
```
