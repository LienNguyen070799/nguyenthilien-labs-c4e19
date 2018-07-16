from gmail import GMail
from gmail import Message
gmail = GMail('nguyenliensera1999@gmail.com','Hustlien070799.')
html_content = """<p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập - tự do -hạnh ph&uacute;c</p>
<h1 style="text-align: center;">ĐƠN XIN NGHỈ HỌC</h1>
<p>K&iacute;nh gửi : Boss Huỳnh Tuấn Anh + Trợ giảng Nguyễn Anh Qu&acirc;n</p>
<p>T&ecirc;n em l&agrave; : Li&ecirc;n</p>
<p>Em l&agrave;m đơn n&agrave;y xin ph&eacute;p được nghỉ học buổi h&ocirc;m nay do {{em bị ốm}}</p>
<p>Em xin hứa sẽ l&agrave;m b&agrave;i đầy đủ</p>
<p>Em xin c&aacute;m ơn!</p>
<p style="text-align: right;">K&yacute; t&ecirc;n</p>
<p style="text-align: right;">LI&Ecirc;N</p>
<p>&nbsp;</p>
"""
reasons = ['em bị đau bụng','anh hàng xóm nhà em lấy vợ','bạn cùng phòng em bị ốm','em buồn ngủ','em không thích đi học','']
from random import choice
reason = choice(reasons)
html_to_send = html_content.replace("{{em bị ốm}}",reason)
from datetime import datetime
now = datetime.now().hour
while now >= 7:
    msg = Message(' Đơn xin nghỉ học', to ='nguyenthilien07071999@gmail.com', html = html_to_send)
    gmail.send(msg)
    break