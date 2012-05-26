# The Grinder 3.9
# HTTP script recorded by TCPProxy at 2012-maj-13 11:59:51

from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
from java.util import Random
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()


# change ADDRESS to where the ESB is running
# change port to query the different use cases
# 8081=proxy, 8082=mediation, 8083=transformation
url0 = 'http://ADDRESS:8081'

# Create an HTTPRequest for each request, then replace the
# reference to the HTTPRequest with an instrumented version.
# You can access the unadorned instance using request101.__target__.
request101 = HTTPRequest(url=url0)
request101 = Test(101, 'POST Echo').wrap(request101)

class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """POST EchoService (request 101)."""
    r = Random()
    val = r.nextInt(3)+1
    
    cnt = 0
    mesg = ''
    # dummy data to generate the wanted amount of payload. adder contains 1024 characters = 1KB.
    adder = 'abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789abcdefghijklmnopqrstuvwxyz 123456789 abcdefghijklmnop'
    
    # change the "while" number to change the size of the message payload, the number represents no of KB, 1 = 1KB, 100= 100KB and so on.
    while (cnt < 1):
      mesg = mesg + adder
      cnt = cnt + 1

    result = request101.POST('/Echo',
      '{"id":"' + str(val) + '" , "message":"' + mesg + '"}',
      ( NVPair('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/15.0 Firefox/15.0a1'),
        NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Accept-Language', 'null'),
        NVPair('Accept-Encoding', 'gzip, deflate'),
        NVPair('Content-Type', 'text/plain; charset=UTF-8'),
        NVPair('Cache-Control', 'no-cache'), ))

    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    self.page1()      # POST Echo (request 101)

def instrumentMethod(test, method_name, c=TestRunner):
  """Instrument a method with the given Test."""
  unadorned = getattr(c, method_name)
  import new
  method = new.instancemethod(test.wrap(unadorned), None, c)
  setattr(c, method_name, method)