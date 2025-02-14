<!DOCTYPE html>
<html>
<head>
    <title>Interactive Treasure Hunt</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div class="container">
        <h2>Welcome to the Interactive Treasure Hunt!</h2>
        <form action="process.php" method="POST">
            <label>Enter a Number:</label>
            <input type="number" name="number" required><br>
            
            <label>Enter a Secret Word:</label>
            <input type="text" name="text" required><br>
            
            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>