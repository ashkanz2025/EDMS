��    (      \  5   �      p     q  B  �    �  "   �     �      �   	  2  �	  u  �
  ^   6  8   �  C   �  �     2  �  �   
  �  �  b   �     �     �     �     �               7     <  
   U     `     g     l     z     �     �     �  d   �     3     B     H     V  x  ^  k  �      C    d  �  l  $   -     R  �   Y  �   X    �  5  �  `   $!  >   �!  F   �!  �   "  �  �"  �   �%  R  M&  Z   �'    �'     )     
)     )     #)     0)     I)     P)     n)     {)     �)     �)     �)     �)     �)     �)  E   �)     -*     :*     >*     K*  \  R*               
      &                                  '                 #         $                        "   (              %          !               	                             "%s" not a valid entry. A dictionary containing the settings for all databases to be used with Django. It is a nested dictionary whose contents map a database alias to a dictionary containing the options for an individual database. The DATABASES setting must configure a default database; any number of additional databases may also be specified. A list of strings representing the host/domain names that this site can serve. This is a security measure to prevent HTTP Host header attacks, which are possible even under many seemingly-safe web server configurations. Values in this list can be fully qualified names (e.g. 'www.example.com'), in which case they will be matched against the request's Host header exactly (case-insensitive, not including port). A value beginning with a period can be used as a subdomain wildcard: '.example.com' will match example.com, www.example.com, and any other subdomain of example.com. A value of '*' will match anything; in this case you are responsible to provide your own validation of the Host header (perhaps in a middleware; if so this middleware must be listed first in MIDDLEWARE). A short text used as the tag name. Default Default: '' (Empty string). Password to use for the SMTP server defined in EMAIL_HOST. This setting is used in conjunction with EMAIL_HOST_USER when authenticating to the SMTP server. If either of these settings is empty, Django won't attempt authentication. Default: '' (Empty string). Username to use for the SMTP server defined in EMAIL_HOST. If empty, Django won't attempt authentication. Default: '/accounts/login/' The URL where requests are redirected for login, especially when using the login_required() decorator. This setting also accepts named URL patterns which can be used to reduce configuration duplication since you don't have to define the URL in two places (settings and URLconf). Default: '/accounts/profile/' The URL where requests are redirected after login when the contrib.auth.login view gets no next parameter. This is used by the login_required() decorator, for example. This setting also accepts named URL patterns which can be used to reduce configuration duplication since you don't have to define the URL in two places (settings and URLconf). Default: 'django.core.mail.backends.smtp.EmailBackend'. The backend to use for sending emails. Default: 'localhost'. The host to use for sending email. Default: 25. Port to use for the SMTP server defined in EMAIL_HOST. Default: 2621440 (i.e. 2.5 MB). The maximum size (in bytes) that an upload will be before it gets streamed to the file system. See Managing files for details. See also DATA_UPLOAD_MAX_MEMORY_SIZE. Default: 2621440 (i.e. 2.5 MB). The maximum size in bytes that a request body may be before a SuspiciousOperation (RequestDataTooBig) is raised. The check is done when accessing request.body or request.POST and is calculated against the total request size excluding any file upload data. You can set this to None to disable the check. Applications that are expected to receive unusually large form posts should tune this setting. The amount of request data is correlated to the amount of memory needed to process the request and populate the GET and POST dictionaries. Large requests could be used as a denial-of-service attack vector if left unchecked. Since web servers don't typically perform deep request inspection, it's not possible to perform a similar check at that level. See also FILE_UPLOAD_MAX_MEMORY_SIZE. Default: False. Whether to use a TLS (secure) connection when talking to the SMTP server. This is used for explicit TLS connections, generally on port 587. If you are experiencing hanging connections, see the implicit TLS setting EMAIL_USE_SSL. Default: False. Whether to use an implicit TLS (secure) connection when talking to the SMTP server. In most email documentation this type of TLS connection is referred to as SSL. It is generally used on port 465. If you are experiencing problems, see the explicit TLS setting EMAIL_USE_TLS. Note that EMAIL_USE_TLS/EMAIL_USE_SSL are mutually exclusive, so only set one of those settings to True. Default: None. Specifies a timeout in seconds for blocking operations like the connection attempt. Default: [] (Empty list). List of compiled regular expression objects representing User-Agent strings that are not allowed to visit any page, systemwide. Use this for bad robots/crawlers. This is only used if CommonMiddleware is installed (see Middleware). Django Edit Edit setting: %s Edit settings Enter the new setting value. Name Namespace: %s, not found Namespaces Revert Save Setting count Setting namespaces Setting updated successfully. Settings Settings in namespace: %s Settings inherited from an environment variable take precedence and cannot be changed in this view.  Smart settings Value View settings Warning When set to True, if the request URL does not match any of the patterns in the URLconf and it doesn't end in a slash, an HTTP redirect is issued to the same URL with a slash appended. Note that the redirect may cause any data submitted in a POST request to be lost. The APPEND_SLASH setting is only used if CommonMiddleware is installed (see Middleware). See also PREPEND_WWW. Project-Id-Version: Mayan EDMS
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2024-01-02 18:58+0000
Last-Translator: Roberto Rosario, 2024
Language-Team: Chinese (Taiwan) (https://app.transifex.com/rosarior/teams/13584/zh_TW/)
Language: zh_TW
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=1; plural=0;
 “%s”不是有效的许可。 包含要与Django一起使用的所有数据库的设置的字典。它是一个嵌套字典，其内容将数据库别名映射到包含单个数据库选项的字典。 DATABASES设置必须配置默认数据库;还可以指定任意数量的附加数据库。 表示此站点可以提供的主机/域名的字符串列表。这是一种防止HTTP主机头攻击的安全措施，即使在许多看似安全的Web服务器配置下也是如此。此列表中的值可以是完全限定名称（例如“www.example.com”），在这种情况下，它们将与请求的主机标头完全匹配（不区分大小写，不包括端口）。以句点开头的值可用作子域通配符：'.example.com'将匹配example.com，www.example.com和example.com的任何其他子域。值'*'将匹配任何内容;在这种情况下，您有责任提供自己的主机头验证（可能在中间件中;如果是这样，则必须首先在MIDDLEWARE中列出此中间件）。 用作标签名称的简短文本。 默认 默认值：''（空字符串）。用于EMAIL_HOST中定义的SMTP服务器的密码。在向SMTP服务器进行身份验证时，此设置与EMAIL_HOST_USER结合使用。如果这些设置中的任何一个为空，Django将不会尝试身份验证。 默认值：''（空字符串）。用于EMAIL_HOST中定义的SMTP服务器的用户名。如果为空，Django将不会尝试身份验证。 默认值：'/ accounts / login /'，重定向请求以进行登录的URL，尤其是在使用login_required（）装饰器时。此设置还接受命名的URL模式，可用于减少配置重复，因为您不必在两个位置（设置和URLconf）定义URL。 默认值：'/ accounts / profile /'，当contrib.auth.login视图没有下一个参数时，登录后重定向请求的URL。例如，login_required（）装饰器使用它。此设置还接受命名的URL模式，可用于减少重复配置，因此您不必在两个位置（设置和URLconf）定义URL。 默认值：'django.core.mail.backends.smtp.EmailBackend'。用于发送电子邮件的后端。 默认值：'localhost'。用于发送电子邮件的主机。 默认值：25。用于EMAIL_HOST中定义的SMTP服务器的端口。 默认值：2621440（即2.5 MB）。上传在流式传输到文件系统之前的最大大小（以字节为单位）。有关详情，请参阅管理文件。另请参见DATA_UPLOAD_MAX_MEMORY_SIZE。 默认值：2621440（即2.5 MB）。引发可疑操作（请求数据太大）之前请求正文的最大大小（以字节为单位）。在访问request.body或request.POST时完成检查，并根据不包括任何文件上传数据的总请求大小计算。您可以将其设置为“无”以禁用检查。预计会收到异常大型表单提交的应用程序应调整此设置。请求数据量与处理请求和填充GET和POST词典所需的内存量相关联。如果不加以检查，大请求可以用作拒绝服务攻击载体。由于Web服务器通常不执行深度请求检查，因此无法在该级别执行类似检查。另请参见FILE_UPLOAD_MAX_MEMORY_SIZE。 默认值：False。与SMTP服务器通信时是否使用TLS（安全）连接。这用于显式TLS连接，通常在端口587上。如果遇到挂起连接，请参阅隐式TLS设置EMAIL_USE_SSL。 默认值：False。与SMTP服务器通信时是否使用隐式TLS（安全）连接。在大多数电子邮件文档中，此类型的TLS连接称为SSL。它通常用于端口465.如果遇到问题，请参阅显式TLS设置EMAIL_USE_TLS。请注意，EMAIL_USE_TLS / EMAIL_USE_SSL是互斥的，因此只将其中一个设置为True。 默认值：无。指定阻塞操作（如连接尝试）的超时（以秒为单位）。 默认值：[]（空列表）。在系统范围内表示不允许访问任何页面的用户代理字符串的已编译正则表达式对象的列表。用于防范恶意的机器人/爬虫。这仅在安装了CommonMiddleware时使用（请参阅Middleware）。 Django 編輯 编辑设定：%s 编辑设置 输入新的设定值。 名称 命名空间：%s，未找到 命名空间 还原 保存 设定计数 设置命名空间 设置已成功更新。 设置 命名空间中的设置：%s 从环境变量继承的设置优先，在此视图中无法更改。 智能设置 值 查看设置 警告 设置为True时，如果请求URL与URLconf中的任何模式都不匹配，并且不以斜杠结尾，则会向相同的URL发出HTTP重定向，并附加斜杠。请注意，重定向可能导致POST请求中提交的任何数据丢失。 APPEND_SLASH设置仅在安装了CommonMiddleware时使用（请参阅Middleware）。另见PREPEND_WWW。 