{% extends "BealsTreasure/bootstrap_dashboard.html" %}

{% block title %}Home{% endblock %}

{% block content %}
<script type="text/javascript" src="{{STATIC_URL}}js/demo.js"></script>

<table>
    <tbody>
    <tr>
        <td>
            <script>
                var scr = document.createElement("script");
                scr.src = "{{STATIC_URL}}js/demo.js" + "?ts=" + new Date().getTime();
                document.getElementsByTagName("head")[0].append(scr);
            </script>
            <center>
                <form method="post">
                    <table border="0" cellpadding="3" cellspacing="0" width="500">
                        <tbody>
                        <tr align="CENTER" valign="bottom">
                            <td colspan="4"><h3>Beal's Treasure Finder 3.0</h3></td>
                        </tr>
                        <tr align="CENTER" valign="bottom">
                            <td colspan="1"><p><input type="button" value="Search!"
                                                      onclick="autocalculateForm(this.form)"></p></td>
                        </tr>
                        </tbody>
                    </table>
                </form>

                <table border="1" cellpadding="3" cellspacing="0" width="500">
                    <tbody>
                    <tr>
                        <td colspan="4" align="center">
                            <img src="http://www.cyberroadie.org/cgi-bin/mathtex.cgi?A%5Ex%20%2B%20B%5Ey%20%3D%20C%5Ez"
                                         alt="A^x + B^y = C^z">
                        </td>
                    </tr>
                    <tr align="center" valign="bottom">
                        <td width="130"><p><b>A</b></p>

                            <p id="A">-</p></td>
                        <td width="130"><p><b>x</b></p>

                            <p id="x">-</p></td>
                        <td width="130"><p><b>B</b></p>

                            <p id="B">-</p></td>
                        <td width="130"><p><b>y</b></p>

                            <p id="y">-</p></td>
                    </tr>
                    <tr align="CENTER">
                        <td colspan="2"><p>Calculator Status:</p></td>
                        <td colspan="2"><p id="status">-</p></td>
                    </tr>
                    <tr align="CENTER">
                        <td colspan="2"><p>Initial Data (%):</p></td>
                        <td colspan="2"><p id="progress1">-</p></td>
                    </tr>
                    <tr align="CENTER">
                        <td colspan="2"><p>Calculating Block (%):</p></td>
                        <td colspan="2"><p id="progress2">-</p></td>
                    </tr>
                    <tr align="CENTER">
                        <td colspan="2"><p>Blocks Solved(test):</p></td>
                        <td colspan="2"><p id="solved">-</p></td>
                    </tr>
                    <tr align="CENTER">
                        <td colspan="2"><p>Code (<a
                                href="/faq/i-found-something/">?</a>):</p></td>
                        <td colspan="2"><p id="prize">undefined</p></td>
                    </tr>
                    </tbody>
                </table>
            </center>
        </td>
        <td>
            <h3 style="text-align: center;">Welcome Aboard Mateys!</h3>

            <p style="text-align: center;">I'm your guide, Captain Joe, let me show you the way to Beal's Treasure, the
                proof that <a title="Conjecture What?" href="/faq/conjecture-what/">Beal's
                    Conjecture</a> is false. </p>
        </td>
    </tr>
    <tr>
        <td colspan="2">
            <br>
        </td>
    </tr>
    <tr>
        <td colspan="2">
            <p style="text-align: center;">If you would like to make a donation to the project, please visit our <a
                    title="Donations" href="/faq/donations/">donation page</a>.</p>
        </td>
    </tr>
    </tbody>
</table>
{% endblock %}