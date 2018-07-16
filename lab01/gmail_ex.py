from gmail import GMail
from gmail import Message
gmail = GMail('nguyenliensera1999@gmail.com','Hustlien070799.')
html_content = """
<p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Đọc lập -tự do - hạnh ph&uacute;c</p>
<p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></p>
<p style="text-align: left;">K&iacute;nh gửi : Boss</p>
<p style="text-align: left;">T&ecirc;n em l&agrave; Nguyễn Thị Li&ecirc;n</p>
<p style="text-align: left;">Em l&agrave;m đơn n&agrave;y xin nghỉ học</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p> 
"""
reason = ["buồn ngủ","ốm", "đói", "không thích đi học", "mệt" ]
from random import choice
reason_1 = choice(reason)
print(reason_1)
html_to_send = html_content.replace("{{sickness}}",reason_1)
# có thể raplace nhiều lần để thay thế nhiều chỗ
msg = Message(' Hello', to ='nguyenthilien07071999@gmail.com', html = html_to_send)
gmail.send(msg)