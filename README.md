# NotionTEN
NotionTEN 是一个基于 Notion 的简单 Todo-list 邮件提醒服务，全称为 Notion Todo Email Notifier。

---
# 背景
我需要日常推送一些零碎的待办事项，但我寻找到的软件都太过庞大。我希望有一个跨平台的、轻量的 Todo-list 服务。于是我选择使用 Notion 与电子邮件的方案，写了我 Github 上第一个项目 NotionTEN。这只是一个简单的程序，一个初学者的练手作，肯定不是最优的解决方案，但的确满足了我的需求，希望对你也能有所帮助。

# 它能做什么？
NotionTEN 的运行过程如下：
1. 获取 Notion 中的数据
2. 筛选其中状态为 `未完成` 的事项
3. 发送邮件到预设邮箱中

这是一个**基于 Notion 的辅助程序**，因此事项的添加、删除、修改仍然需要在 Notion 中完成。如果你不习惯使用 Notion 来管理任务，我**推荐**还是使用其他 Todo 软件。

我**不建议**你用NotionTEN来做以下的事情：
- 重要事项的项目管理
- 周期性事务的提醒

NotionTEN 是针对一些日常琐事开发的，对于以上这类事情，你可以尝试换用更专业、功能更完善的软件。

# 使用
0. 复制我的 [模板](https://woodash.notion.site/woodash/7d9f4c563e4c4ce8844729f62acbbe02)，以避免出现某些潜在问题。
1. 创建一个 [Notion API](https://www.notion.so/my-integrations)，并点击页面右上方的三点，选择 Add connections 绑定到 database。
2. Fork 这个仓库，并在 Settings 中开启 Github Action 的运行。
3. 在仓库设置中添加对应 secrets。

# Secrets
## Notion 相关
`DATABASEID` 你的数据库 ID，包含于页面链接中。
> 页面链接可能是如下的形式：
> ```
> https://www.notion.so/yourname/xxxxxxxx?v=oooooooo
> ```
> 需要注意，你需要的 `DATABASEID` **仅仅是 `?v=` 前面的部分**，也就是 `xxxxxxxx`，**请勿**填入之后的部分。  

`TOKEN` 你创建的 Notion API 的密钥。  

## 邮件相关
`SENDER` 你的发件邮箱地址。

`PASSWORD` 你的发件邮箱授权码，**可能**为你的登陆密码。

`RECEIVER` **（可选）** 你的收件邮箱地址，不设置则默认为 `SENDER` 邮箱向自己发送邮件。

`PORT` 你的发件邮箱的 SMTP 端口，请在邮箱设置内查询。

`SMTPSERVER` 你的发件邮箱的 SMTP服务器地址 ，请在邮箱设置内查询。

# 注释
- 由于 Github Action 与邮箱的延迟，邮件可能并不会在设置的时间准时送达，但是作为每日的提醒应该是足够的。 
- 模板内有一个名为 `标题` 的函数项，是为了方便实现功能创建的，保持隐藏即可，请勿删除。
- 为了简洁，我选择设定默认视图为未完成事项的表格，如果你想查看自己都做过什么，可以切换视图看看，也可以自己设置需要的视图。
- 你可以任意更改标题、图标、背景、评论权限等大部分设置，除了表格中的属性，也就是 `日期`、`项目`、`完成状态` 这几项。详情请看接下来的[高级设置](#高级设置)。
- Notion 中的日期有持续日期与包含时间的详细日期，但我并没有测试，可能会导致一些问题。如果你觉得有必要加上，欢迎在 issue 中提出，我会考虑适配。

# 高级设置
若是要修改数据库的属性，请在修改后在 secrets 中也进行对应配置。实际上，如果你不是特别在意每一栏的标题，我建议还是不要修改，因为这可能会导致一些问题。

 `NOTION_DATE`  你在 Notion 中更改的日期的名称。默认为“日期”。  
 `NOTION_STATUS`  你在 Notion 中更改的状态的名称，默认为“完成状态”。

---
你可以在 `/.github/workflows/NotionTEN.yaml` 中修改定期运行时间。格式如下：
```yaml
schedule:
  - cron: '0 10,23 * * *'
```
时间使用 cron 格式，默认为在北京时间 7 点及 18 点运行。如果你仅需要更改运行的小时，将 24 小时制的北京时间减去 8 小时填入，更复杂的用法请自行查询。

---
你也可以修改时区，这会影响程序对当前日期的获取，默认为 `Asia/Shanghai` 。
```yaml 
- name: Setup timezone
        uses: szenius/set-timezone@v1.0
        with:
          timezoneLinux: "Asia/Shanghai"
```

# 计划任务
- [ ] 英文文档
- [ ] 更优雅的邮件样式
- [ ] 可能会有一个 logo

