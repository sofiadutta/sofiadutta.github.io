<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="html" version="5.0" encoding="UTF-8" indent="yes" />
  <xsl:template match="/">
    <html>
      <body>
        <h2>UMBC <xsl:value-of select="/schedule/@semester" />, <xsl:value-of select="/schedule/@year" /> Course Schedule</h2>
        <table>
          <xsl:for-each select="schedule/course">
            <tr bgcolor="#A569BD" align="center">
              <td>
                <b>
                  <xsl:value-of select="programIdentifier" /> - <xsl:value-of select="number" /></b>
              </td>
            </tr>
            <tr bgcolor="##F7DC6F" align="left">
              <td>
                <b>Title : <xsl:value-of select="title" /></b>
              </td>
            </tr>
            <tr align="left">
              <td>
                <b>Credit : </b>
                <xsl:value-of select="credit" />
              </td>
            </tr>
            <tr align="left">
              <td>
                <b>Description : </b>
                <br />
                <xsl:value-of select="description" />
              </td>
            </tr>
            <tr align="left">
              <td>
                <b>Prerequisite : </b>
                <xsl:value-of select="prerequisite" />
              </td>
            </tr>
            <tr bgcolor="#3498DB" align="center">
              <td>
                <b>Sections</b>
              </td>
            </tr>
            <xsl:for-each select="section">
              <tr>
                <td>
                  <b>Section Number : </b>
                  <xsl:value-of select="sectionNumber" />
                </td>
              </tr>
              <tr>
                <td>
                  <b>Instructor : </b>
                  <xsl:value-of select="instructor" />
                </td>
              </tr>
              <tr>
                <td>
                  <b>Class Number : </b>
                  <xsl:value-of select="classNumber" />
                </td>
              </tr>
              <tr>
                <td>
                  <b>Meets : </b>
                  <xsl:value-of select="days" /> - <xsl:value-of select="startTime" /> - <xsl:value-of select="endTime" /></td>
              </tr>
              <tr>
                <td>
                  <b>Room : </b>
                  <xsl:value-of select="room" />
                </td>
              </tr>
              <tr>
                <td>
                  <b>Status : </b>
                  <xsl:value-of select="status" />
                </td>
              </tr>
              <tr bgcolor="#9acd32">
                <td>
                  <b>
                  </b>
                </td>
              </tr>
            </xsl:for-each>
            <tr bgcolor="#924363">
              <td>
                <b>
                </b>
              </td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
