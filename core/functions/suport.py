from datetime import datetime
import os



class Functions:
    
    def convertDT(date_in):
        if type(date_in)==str:
            x = date_in.replace("T"," ") 
            x = x.replace("Z","")
            date_time = datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
            return date_time
        else:
            return date_in

    def convertSTR(datetime_in):   
        string = datetime.strftime(datetime_in, "%Y-%m-%dT%H:%M:%SZ")
        return string

    def validate_url(host, protocol):
            if protocol not in host:
                return protocol + host
            else:
                return host
    def boolean(in_arg):
        if str(in_arg).lower() == 'true':
            return True
        else:
            return False


    