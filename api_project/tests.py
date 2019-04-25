import pymysql,hashlib
def test_md5(value):
    md5=hashlib.md5()
    md5.update(value.encode("utf-8"))
    return str(md5.hexdigest())
cnn=pymysql.connect(host="127.0.0.1",db="api_project",port=3306,user="root",password="root3306")
cur=cnn.cursor()
sql="insert into api_project_userinfo(username,password,userimage_url,usertype) values ('wenx','e10adc3949ba59abbe56e057f20f883e','ww.baidu.com','1')"
print(sql)
cur.execute(sql)
cnn.commit()