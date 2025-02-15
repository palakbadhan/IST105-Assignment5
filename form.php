<!DOCTYPE html>
<html>
<head>
    <title>Interactive Treasure Hunt</title>
    <style>
        .container {
            width: 50%;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            text-align: center;
            background: #f9f9f9;
            font-family: Arial, sans-serif;
        }
        input {
            display: block;
            margin: 10px auto;
            padding: 10px;
            font-size: 16px;
            width: 80%;
        }
        input[type="submit"] {
            background: #007bff;
            color: #fff;
            border: none;
            cursor: pointer;
            padding: 12px;
            font-size: 18px;
            border-radius: 5px;
        }
        input[type="submit"]:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Welcome to the Interactive Treasure Hunt!</h2>
        <form action="process.php" method="POST">
            <label>Enter a Number:</label>
            <input type="number" name="number" required><br>
            
            <label>Enter a Secret Word:</label>
            <input type="text" name="text" required><br>
            
            <input type="submit" value="Solve the puzzle">
        </form>
    </div>
</body>
</html>
