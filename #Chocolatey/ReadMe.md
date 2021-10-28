# Chocolatey

## Packages.config

Use [packages.config](./packages.config) file to batch install all essential apps

    choco install packages.config

- [Remove versions](https://stackoverflow.com/questions/43167087/how-to-get-a-list-of-packages-from-one-machine-and-install-in-another-with-choco#:~:text=Here%27s%20a%20fast%2C%20easy%20way%20to%20remove%20the%20versions) from packages.config file 
    - <details>
        <summary>Remove versions from packages.config file</summary>

        ```xsl
        <!-- Undying credit to Mads Hanser: https://stackoverflow.com/a/3117549/5432315 -->
        <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
            <!--empty template suppresses this attribute-->
            <xsl:template match="@version" />
            <!--identity template copies everything forward by default-->
            <xsl:template match="@*|node()">
                <xsl:copy>
                    <xsl:apply-templates select="@*|node()"/>
                </xsl:copy>
            </xsl:template>
        </xsl:stylesheet>
        ```
        </details>
