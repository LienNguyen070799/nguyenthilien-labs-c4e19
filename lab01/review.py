from gmail import GMail, Message
gmail = GMail('nguyenliensera1999@gmail.com','Hustlien070799.')
msg = Message('welcome',to ='nguyenthilien07071999@gmail.com',html = '<h1>chào em.kaka</h1>')
gmail.send(msg)
