<?php
    $res=(new mysqli("localhost","root","","cars"))->query("SELECT * FROM sales");
    echo "<table border='1'>
            <tr>
                <th>ID</th>
                <th>Products</th>
                <th>Value</th>
                <th>Discription</th>
            </tr>";
    while($r=$res->fetch_assoc())
        echo "<tr>
                <td>$r[ID]</td>
                <td>$r[Product]</td>
                <td>$r[Value]</td>
                <td>$r[Discription]</td>
            </tr>";
    echo "</table>";
?>