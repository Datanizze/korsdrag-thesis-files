package se.datanizze.korsdrag.webservice.server;

import javax.xml.ws.Endpoint;

import se.datanizze.korsdrag.webservice.ws.EchoServiceImpl;

/**
 * Hello world! with help from http://www.mkyong.com/webservices/jax-ws/jax-ws-hello-world-example-document-style/
 * 
 */
public class WSPublisher { // uses jetty

    private static final String SERVICE_URL = "http://0.0.0.0:6587/EchoService";
    private static Endpoint echoEndpoint = null;

    public static void main(String[] args) {
        System.out.println("Initializing EchoService Endpoint");
        echoEndpoint = Endpoint.create(new EchoServiceImpl());
        System.out.println("Publishing Endpoint");
        echoEndpoint.publish(SERVICE_URL);
        System.out.println("Echo Service Started at " + SERVICE_URL);

    }
}
