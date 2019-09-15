<!--  Edited with XML -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
	<xsl:template match="/">
		<html>
			<head>
				<title>
						<h2>UMBC Fall Course Schedule</h2>
				</title>
			</head>
			<body>
				<xsl:for-each select="schedule/course">
					<b><xsl:value-of select="programIdentifier"/>
					<xsl:value-of select="number"/></b><br/>
					<b><xsl:value-of select="title"/></b><br/>
					<b>Prerequisite : </b><xsl:value-of select="prerequisite"/></br>
					<b>Description : </b><br><xsl:value-of select="description"/></br>
					<xsl:for-each select="schedule/course/section">
						<b>Sec- </b><xsl:value-of select="sectionNumber"/></br>
						<b>Instructor : </b><xsl:value-of select="instructor"/></br>
						<b>Schedule Number : </b><xsl:value-of select="scheduleNumber"/></br>
						<b>Room : </b><xsl:value-of select="room"/></br>
						<b>Day : </b><xsl:value-of select="day"/></br>
						<b>Time : </b><xsl:value-of select="startTime"/> - <xsl:value-of select="endTime"/></br>
						<b>Status : </b><xsl:value-of select="status"/></br>
					</xsl:for-each>
				</xsl:for-each>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>