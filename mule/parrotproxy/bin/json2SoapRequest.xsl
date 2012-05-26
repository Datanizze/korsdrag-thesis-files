<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
        
	<xsl:template match="/">
		<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
			xmlns:ws="http://ws.webservice.korsdrag.datanizze.se/">
			<soapenv:Header />
			<soapenv:Body>
				<ws:echoMessage>
					<id><xsl:value-of select="//entry[1]//__value" /></id>
					<message><xsl:value-of select="//entry[2]//__value" /></message>
				</ws:echoMessage>
			</soapenv:Body>
		</soapenv:Envelope>

	</xsl:template>

</xsl:stylesheet>