<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes" />
    <xsl:template match="/">
        <html>
		        <body>
		            <h2>UMBC <xsl:value-of select="/schedule/@semester"/>, <xsl:value-of select="/schedule/@year" /> Course Schedule</h2>
		            <table border="1">
		                <xsl:for-each select="schedule/course">
		                    <tr>
		                        <td><b>Program</b>
		                            <th align="right">
		                                <xsl:value-of select="programIdentifier" />
		                            </th>
		                        </td>
		                    </tr>
		                    <tr>
		                        <td><b>Course Number</b></td>
		                        <td>
		                            <xsl:value-of select="number" />
		                        </td>
		                    </tr>
		                    <tr>
		                        <td><b>Title</b></td>
		                        <td>
		                            <xsl:value-of select="title" />
		                        </td>
		                    </tr>
		                    <tr>
		                        <td><b>Prerequisite</b></td>
		                        <td>
		                            <xsl:value-of select="prerequisite" />
		                        </td>
		                    </tr>
		                    <tr>
		                        <td><b>Description</b></td>
		                        <td>
		                            <xsl:value-of select="description" />
		                        </td>
		                    </tr>
		                    <tr>
		                        <td><b>Sections</b></td>
		                    </tr>
		                    <xsl:for-each select="section">

		                        <tr>
		                            <td><b>Section Number</b></td>
		                            <td>
		                                <xsl:value-of select="sectionNumber" />
		                            </td>
		                        </tr>
		                        <tr>
		                            <td><b>Instructor</b></td>
		                            <td>
		                                <xsl:value-of select="instructor" />
		                            </td>
		                        </tr>
		                        <tr>
		                            <td><b>Class Number</b></td>
		                            <td>
		                                <xsl:value-of select="classNumber" />
		                            </td>
		                        </tr>
		                        <tr>
		                            <td><b>Room</b></td>
		                            <td>
		                                <xsl:value-of select="room" />
		                            </td>
		                        </tr>
		                        <tr>
		                            <td><b>Days</b></td>
		                            <td>
		                                <xsl:value-of select="days" />
		                            </td>
		                        </tr>
		                        <tr>
		                            <td><b>Start Time</b></td>
		                            <td>
		                                <xsl:value-of select="startTime" />
		                            </td>
		                        </tr>
		                        <tr>
		                            <td><b>End Time</b></td>
		                            <td>
		                                <xsl:value-of select="endTime" />
		                            </td>
		                        </tr>
		                        <tr>
		                            <td><b>Status</b></td>
		                            <td>
		                                <xsl:value-of select="status" />
		                            </td>
		                        </tr>
		                        <tr bgcolor="#9acd32">
		                            <td><b>      </b></td>
		                            <td><b>      </b></td>
		                        </tr>
		                    </xsl:for-each>
		                    <tr bgcolor="#9acd32">
		                        <td><b>      </b></td>
		                        <td><b>      </b></td>
		                    </tr>
		                </xsl:for-each>
		            </table>
		        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
