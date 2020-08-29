import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])
# Example
if __name__ == '__main__':
    a=['tk','sys','shutil','csv','numpy','pandas','datetime','time','webbrowser','PIL','smtplib','email','subprocess','cv2','setup','idna','cx_Freeze']

    for i in range(len(a)):
        install(a[i])



    '''
    install('tk')
    install('sys')
    install('shutil')
    install('csv')
    install('numpy')
    install('pandas')
    install('datetime')
    install('time')
    install('webbrowser')
    install('PIL')
    install('smtplib')
    install('email')
    #install('MIMEText')
    #install('MIMEBase')
    #install('encoders')
    install('subprocess')
    install('cv2')
    install('setup')
    install('idna')
    install('cx_Freeze')

'''