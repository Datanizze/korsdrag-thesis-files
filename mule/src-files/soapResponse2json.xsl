
<xsl:stylesheet version="2.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
	<xsl:output method="text" version="1.0" encoding="UTF-8"
		indent="no" omit-xml-declaration="yes" />
	<xsl:template match="/">
		<xsl:text>{"response":"</xsl:text>
		<xsl:value-of select="//WSResponse" />
		<xsl:text>"}</xsl:text>

	</xsl:template>

</xsl:stylesheet>