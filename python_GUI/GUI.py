from tkinter import *
import boto3
from botocore.exceptions import ClientError
from secret import access_key, secret_access_key
from boto3.session import Session
from PIL import ImageTk,Image
import matlab.engine
def save_info():
    client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)
    bucket = 'projectyazan'
    D2_info = D2_string.get()
    LDR_info = LDR_string.get()
    HUM_info = HUM_string.get()
    TEMP_info = TEMP_string.get()
    print(D2_info,LDR_info,HUM_info,TEMP_info)
    file = open("threshold.txt","w")
    file.write(str(D2_info))
    file.write("\n")
    file.write(str(LDR_info))
    file.write("\n")
    file.write(str(HUM_info))
    file.write("\n")
    file.write(str(TEMP_info))
    file.write("\n")
    file.close()
    client.upload_file("threshold.txt", bucket, 'project/threshold.txt')


def read_data():
    client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)
    bucket = 'projectyazan'
    client.download_file(bucket,'project/output.txt', 'result.txt')
    new_window = Toplevel(app)
    new_window.geometry("500x500")
    lbl= Label(new_window,text="here are the current sensor variables from the greenhouse",bg="green",fg="black",font = "12",width="500",height="3")
    lbl.pack()
    with open("result.txt", "r") as a_file:
        i=1
        for line in a_file:
            info = Label(new_window,text=line)
            info.place(x=15, y = 70*i)
            info.pack()
            i=i+1
        a_file.close()

def diagnose():
    eng = matlab.engine.start_matlab()
    eng.cd(r'C:\Users\Skuzm_Shradar\Desktop\Final_Project\Leaf-Disease-Detection-Using-SVM-Classifier-master\Plant_Diseases_Detection', nargout=0)
    eng.ls(nargout=0)
    eng.Multi_SVM(nargout=0)
    
def display_disease():
    client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)
    bucket = 'projectyazan'
    client.download_file(bucket,'project/detection.jpg', 'detection.png')
    new_window = Toplevel(app)
    new_window.geometry("500x500")
    lbl= Label(new_window,text="heres the latest snapshot from inside the greenhouse",bg="green",fg="black",font = "12",width="500",height="3")
    lbl.pack()   
    detection = ImageTk.PhotoImage(Image.open("detection.png"))
    detection_label= Label(new_window,image=detection)
    detection_label.photo = detection
    detection_label.pack()
    MATLAB=Button(new_window, text="Diagnose",command=diagnose,width="30",height="2",bg="white")
    directions= Label(new_window,text="directions to test for diagnoses" + '\n'
     + "1) click the diagnose button"+ '\n' 
     + "2)choose suspected disease" + '\n' 
     + "3) the MATLAB will display the suspected disease and the accuracy percentage")
    directions.pack()
    MATLAB.pack()




app = Tk()
app.geometry("500x500")
app.title("green house monitoring and control")
heading = Label(text="please enter desired threshold values",bg="green",fg="black",font = "12",width="500",height="3")
heading.pack()
D2 = Label(text="enter gas sensor threshold")
LDR = Label(text="enter LDR sensor threshold")
HUM = Label(text="enter humidity sensor threshold")
TEMP = Label(text="enter tempreture sensor threshold")
D2.place(x=15,y=70)
LDR.place(x=15,y=140)
HUM.place(x=15,y=210)
TEMP.place(x=15,y=280)
D2_string = IntVar()
LDR_string = IntVar()
HUM_string = IntVar()
TEMP_string = IntVar()
D2_entry= Entry(textvariable=D2_string,width="30")
LDR_entry= Entry(textvariable=LDR_string,width="30")
HUM_entry= Entry(textvariable=HUM_string,width="30")
TEMP_entry= Entry(textvariable=TEMP_string,width="30")
D2_entry.place(x=15,y=90) 
LDR_entry.place(x=15,y=160) 
HUM_entry.place(x=15,y=230) 
TEMP_entry.place(x=15,y=300) 
button=Button(app, text="Submit Values",command=save_info,width="30",height="2",bg="white")
button.place(x=15,y=400)
read_button= Button(app,text="read current data from geenhouse", command=read_data,width = "30", height="2", bg ="white")
read_button.place(x=250,y=400)
read_button= Button(app,text="display latest snapshot of the greenhouse", command=display_disease,width = "30", height="2", bg ="white")
read_button.place(x=250,y=450)
mainloop()