import smtplib
import json
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


def remplir_html(numero,email,nom,):

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <title>Document</title>
    
    </head>
    <body>
        <p> Numero :"""+numero+ """</p>
        <p> Nom :"""+nom+ """</p>
        <p> Email :"""+email+ """</p>

    </body>
    <style>

        
    @media screen and (max-width: 1400px) {
    .container{
        width: 100%;
        height: auto;
        display: flex;
        flex-direction: column;
        background-color: rgba(209, 205, 205, 0.526);
        opacity: 0.7;
        border-radius: 5px;
    }
    }
    @media screen and (min-width:1550px) {
        .container{
            width: 80%;
            height: auto;
            display: flex;
            flex-direction: column;
            background-color: rgba(209, 205, 205, 0.526);
            opacity: 0.7;
            border-radius: 5px;
        }
    }
    
        .line{
            width: 100%;
            margin-top: 2%;
            background-color: #fff;
            height: 4px;
            
        }
        .dernier{
            padding: 4%;
            display: flex;
            flex-direction: column;
        }
        .collabs{
            display: flex;
            justify-content: space-around;
        }
        .coll{
            width: 80%;
            height: auto;
        }
        .coll h6{
            font-size: 15px;
            color: grey;
            font-family: 'Century Gothic';
        }
        .item{
            border-radius: 50%;
            width:65px;
            margin-top: 90px;
            height: 65px;
            display: flex;
            justify-content: center;

        }
        .item p{
            font-family: 'Century Gothic';
            font-size: 23px;
            color: #fff;
            margin-top: 23%;
        }
        .red{
            background-color: rgb(196, 118, 2);
        }
        .green img{
            margin-top: 10px;
            border-radius: 50%;
        }
        .footer{
            display: flex;
            justify-content: center;
        }
        .footer p{
            font-family: 'Century Gothic';
        }
        .footer label{
            font-family: 'Century Gothic';
        }
        .footer form{
            margin-top: 2%;
            margin-left: 5%;
        }
        .blanc{
            background-color: #fff;
            margin-left: 3%;
            margin-right: 3%;
            margin-top: 6%;
            padding: 5%;
            margin-bottom: 3%;
        }
        .blanc .btn{
            width: 40%;
            height: 40px;
            color: #fff;
            background-color: rgb(36, 61, 97);
            cursor: pointer;
        }
        .entete div{
            width: 100%;
            display: flex;  
            justify-content: end;
            padding: 3px 3px 3px 5px;
            position: relative;
            right: 18px;
            border: none;
            margin-top: 4%;
        }
        .entete div i{
            margin-top: 10px;
            padding-left: 7px;
        }
        .entete div p{
            color: rgb(54, 53, 53);
            font-family:Arial, Helvetica, sans-serif;
            font-size: smaller; 
        }
        .blue{
            width: 100%;
            height: 10px;
            background-color: blue;
        }
        .beige{
            background-color: rgb(212, 232, 255);
            padding: 4%;
            display: flex;
            justify-content: space-around;
        }
        .beige .gauche .p_g{
            font-size: 18px;     
            font-weight: 600; 
        }
        
        .droite{
            display: flex;
            width:63px;
            height: 53px;
            margin-top: 90px;
            padding-top:5px ;
            border-radius: 50%;
            background-color: rgb(3, 87, 3);
            justify-content: center;

        }
        .droite p{
            margin-top: 14px;
            font-size: 18px;
            font-family: 'Century Gothic';
            color: #fff;

        }
    </style>
    <script>
     var btn = document.querySelector('.btn')

     btn.addEventListener("click", ()=>{
     window.location.replace('')
     })
    </script>
    </html>
    """

    return html



#formataddr(('Support bksd',"outlookmicrosoft33@gmail.com"))
gmail_cfg = {
    "server":"smtp.gmail.com",
    "port":"465",
    "email":"airplayce@gmail.com",
    "pwd": "oowznnhrtzobpcfp"
    
 }

def envoi_mail(nom,email,numero):

    msg = MIMEMultipart("alternative")
    msg['from'] = formataddr(('Airplayce',"bhalesilvere@gmail.com"))
    msg['Subject'] = "[Urgent] Client: Ajout de nouveau"
    msg['to'] = "bhalesilvere@gmail.com"

    html = remplir_html(numero=numero,nom=nom,email=email)

    part = MIMEText(html, "html")

    msg.attach(part)


    with smtplib.SMTP_SSL(gmail_cfg['server'],gmail_cfg['port']) as smtp :
        smtp.login(gmail_cfg['email'],gmail_cfg['pwd'])
        smtp.send_message(msg)
    print("envoyé...")
    