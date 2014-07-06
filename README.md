FlaskBluePrintDemo with sub domain
==================

Flask 配置BluePrint 子域名 项目结构

# 内含
* 使用 BluePrint 配置多模块 Flask 项目
* 支持同一域名下子域名关联BluePrint模块
* BluePrint 模块配置, 初始化中配置static和templates路径

# 运行项目
* python BluePrintDemo.py
* 在hosts中增加  127.0.0.1 sub.xyz.com xyz.com
* 浏览器访问 http://www.xyz.com or http://sub.xyz.com

# requirement
* Flask==0.10.1
* Jinja==2.7.2

# keywords
* Flask
* BluePrint
* sub_domain subdomain
* project structure
