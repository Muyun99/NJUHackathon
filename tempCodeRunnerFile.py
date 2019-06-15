st',  # 本地数据库
                           user='root',  # 用户名
                           passwd='123456',  # 数据库密码
                           db='library',  # 数据库名
                           charset='utf8')
    cursor = conn.cursor()
    rowcount = cursor.execute("select * from library_book")
    #row1 = cursor.fenthone()
    print(rowcount)

    

    # sql = "insert into library_book(url, time) values('%s','%s')" % (Url，Time)
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    # except Exception,e:
    #     db.rollback() #发生错误时回滚
    #     print(e)
    # cursor.close()

    for i in range(100000):
        url = "http://www.cnpub.com.cn/2019/"
        index += 1
        url = url + str(index) + ".html"
        print(url)
        code = requests.get(url)
        soup = BeautifulSoup(code.text, "html.parser")
        title = soup.title
        p = soup.html.find_all('p')
        templist = title.string.split('-')
        bookname = templist[0].strip()
        publisher = templist[1].split('/')[0].strip()
        ISBN = p[3].string.split("：")[1].strip().replace('-', '')
        Author = p[0].string.split("：")[1].strip()
        print(index)
        print(bookname)
        print(publisher)
        print(Author)
        print(ISBN)
        print()

        try:
        # 执行一条insert语句，返回受影响的行数
        # cursor.execute("INSERT INTO para5(name,age) VALUES(%s,%s);",('次牛','12'))
        # 执行多次insert并返回受影响的行数
            sql = "insert into library_book(book_name, publisher,isbn,author,book_count,book_remark) values('%s','%s','%s','%s','%d','%s')" % (
                bookname, publisher, ISBN, Author, int(random.random() * 10) + 1, bookname + "是一本不错的书")
            cursor.execute(sql)
            conn.commit()
            print("写入成功!!!!!!")
        except Exception as e:
            # 如果执行sql语句出现问题，则执行回滚操作
            conn.rollback()
            print("插入异常!!!!!!")
            print(e)
       
    conn.commit()
    cursor.close()
    # print(p[0].string)
    # print(p[3].string)
    # print(code.text)


if __name__ == '__main__':
    getBookInfo()
