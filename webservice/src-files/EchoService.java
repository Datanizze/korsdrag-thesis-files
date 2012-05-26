package se.datanizze.korsdrag.webservice.ws;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;
import javax.jws.soap.SOAPBinding.Use;

@WebService(name = "echoService")
@SOAPBinding(style = Style.DOCUMENT, use = Use.LITERAL)
public interface EchoService {

    @WebMethod
    String echoMessage(int id, String message);
}
