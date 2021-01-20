
import tkinter as tk
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import server_config
from tkinter import messagebox

host = server_config['host']
port = server_config['port']

RIGHT = tk.RIGHT
TOP = tk.TOP
LEFT = tk.LEFT
X = tk.X

def sendMail():
    idd = ID.get()
    cstname = CSTName.get()
    ip = IP.get()
    mbps = Mbps.get()
    username = user_name.get()
    password = pass_word.get()
    message = MIMEMultipart("alternative")
    to = 'eslam.abdelaziztaha@vodafone.com'
    cc = ''
    body = """<html>
<body><font color="#0056D3">
Dears,<br>
&nbsp;&nbsp;&nbsp;&nbsp;Kindly check the below alert,<br><br>
<p>CST Name: <font color="#00D31D">"""+cstname+"""</font><br>
Impacted destination IP: <font color="#00D31D">"""+ip+"""</font><br>
Attack volume: <font color="#00D31D">"""+mbps+""" Mbps</font><br>
DSS confirmation to take action:<br>
Security confirmation that attack is still exist:<br></p></font>
<p>Best Regards<br>
Nabhan Mohamed</p>
</body>
</html>
    """
    mailbody = MIMEText(body, "html")
    message.attach(mailbody)
    context = ssl.create_default_context()
    message["Subject"] = "DDOS Attack || "+cstname+" || "+ip+" || "+idd
    message["From"] = "nabhan.mohamedahmed@vodafone.com"
    message["To"] = to
    message['Cc'] = cc
    rcpt = [cc]+[to]
    try:
        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(username, password)
        server.sendmail(message["From"], rcpt, message.as_string())
    except Exception as e:
        errorMSG(e)
    finally:
        server.quit()

def errorMSG(e):
    messagebox.showinfo("Error", e)
    
def server_settings():
    settings = tk.Toplevel()
    settings.geometry("250x100")
    settings.title('Server Settings')
    def setting_save():
        server_config['host'] = server_ent.get()
        server_config['port'] = port_ent.get()
        try:
            with open('config.py', 'w') as conff:
                conff.write("server_config = {'host':'"+server_config['host']+"','port':'"+server_config['port']+"'}")
            messagebox.showinfo("Info", "Saved Successfully")
            root.quit
        except IOError as io:
            errorMSG(io)
        root.quit
    row = tk.Frame(settings)
    lab = tk.Label(row, text="Host/IP: ", anchor='w')
    server_ent = tk.Entry(row)
    server_ent.insert(0, server_config['host'])
    server_ent.pack(side=RIGHT)
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    lab.pack(side=LEFT)

    row = tk.Frame(settings)
    lab = tk.Label(row, text="Port: ", anchor='w')
    port_ent = tk.Entry(row)
    port_ent.insert(0, server_config['port'])
    port_ent.pack(side=RIGHT)
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    lab.pack(side=LEFT)

    row = tk.Frame(settings)
    save_button = tk.Button(row, text="Save", command=setting_save)
    save_button.pack(side=LEFT, padx=5, pady=5)
    quit_button = tk.Button(row, text="Close", command=settings.destroy)
    quit_button.pack(side=RIGHT, padx=5, pady=5)
    row.pack(side=TOP, fill=X, padx=5)

root = tk.Tk()
root.title("Mailer")
root.geometry("210x295")

ID_label = tk.Label(text="ID: ")
ID = tk.Entry()
ID_label.pack()
ID.pack()
CSTName_label = tk.Label(text="CST Name: ")
CSTName = tk.Entry()
CSTName_label.pack()
CSTName.pack()
IP_label = tk.Label(text="IP: ")
IP = tk.Entry()
IP_label.pack()
IP.pack()
Mbps_label = tk.Label(text="Mbps: ")
Mbps = tk.Entry()
Mbps_label.pack()
Mbps.pack()
user_label = tk.Label(text="domain\\Username: ")
user_name = tk.Entry()
user_label.pack()
user_name.pack()
password_label = tk.Label(text="Password: ")
pass_word = tk.Entry(show='*')
password_label.pack()
pass_word.pack()
send_mail_button = tk.Button(text="Send Mail", command=sendMail)
send_mail_button.pack()
b5 = tk.Button(text = "Settings",command=server_settings)
b5.pack()

root.mainloop()
