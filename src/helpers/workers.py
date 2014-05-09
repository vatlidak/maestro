'''
Workers API
'''
import pickle
import redis
import subprocess
import  os

class Worker():
    '''Constructor of class'''
    def __init__(self, host_port='', channel=''):
        # get arguments
        try:
            self.host = host_port.split(':')[0]
            self.port = host_port.split(':')[1]
            if not channel:
                self.channel = 'maestro_channel'
            else:
                self.channel = channel
        except Exception, error:
            print "Malformed IP:PORT pair:\"%s\"" % ip_port
            print error
            return

        # instanciate pool
        try:
            self.connection_pool = redis.Redis(self.host, self.port)
            print "Connection pool at: <%s:%s>" % (self.host, self.port)
        except Exception, error:
            print "Failed to launch ConnectionPool"
            print error
            return
         
        #subscribe to channel
        try:
            self.pubsub = self.connection_pool.pubsub()
            self.pubsub.subscribe(self.channel)
        except Exception,  error:
            print "Unable to subscribe to channel"
            print error
            return

        # start polling for messages
        print "Polling for messages:"
        for item in self.pubsub.listen(): 
            if item['type'] == 'message' and item['channel'] == self.channel:
                print item
                self._action(item)

    def _action(self, item):
       
        # decode msg body
        msg = pickle.loads(item['data'])
        
        #parse message
        job_key = msg['job_key']
        arguments = msg['job_arguments'].split(' ')[:]
        script_body = msg['script_body']

        # create temp file
        f = open("this_will_never_exist.sh", "w+")
        f.write(script_body)
        f.close()

        # execute command
        pcommand = ['bash', 'this_will_never_exist.sh'] + arguments
        s = subprocess.Popen(pcommand, stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE)
        # get return values
        stdout, stderr = s.communicate()
        errno = s.returncode

        # remove temp file
        os.remove("this_will_never_exist.sh")
        

        
        print "arguments:\n", arguments
        print "body:\n", script_body
        print "stdout:", stdout
        print "stderr:",stderr
        print "errno:", errno
        print "key:", job_key
#
if __name__ == "__main__":
    w = Worker("localhost:6379")
    print w
