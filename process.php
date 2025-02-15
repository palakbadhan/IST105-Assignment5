<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $number = escapeshellarg($_POST['number']);
    $text = escapeshellarg($_POST['text']);
    
    $output = shell_exec("python3 process.py $number $text 2>&1");
    
    echo "<div class='container'><h2>Results</h2>";
    echo "<p>" . nl2br(htmlspecialchars($output)) . "</p>";
    echo "</div>";
}
?>

