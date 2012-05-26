package se.datanizze.korsdrag.webservice.ws;

import javax.jws.WebParam;
import javax.jws.WebResult;
import javax.jws.WebService;

@WebService
public class EchoServiceImpl implements EchoService {

    private static final String appendedString = "This is a string added by the Web Service";

    @Override
    @WebResult(name = "WSResponse")
    public String echoMessage(@WebParam(name = "id") int id, @WebParam(name = "message") String message) {
        System.out.println("Incoming!" + System.currentTimeMillis());
        String ret = String.format("%d. %s \n %s", id, message, appendedString);
        return ret;
    }
}