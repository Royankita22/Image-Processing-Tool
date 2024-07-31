<?php
session_start();

$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "ala";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Validate input
    if (empty($email) || empty($password)) {
        echo "Username and password are required!";
        exit();
    }

    // Hash the password
    #$hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Connect to database
    $conn = mysqli_connect("localhost", "username", "password", "ala");

    // Check connection
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }

    // Check if username already exists
    $check_username_query = "SELECT * FROM login WHERE email='$email'";
    $check_username_result = mysqli_query($conn, $check_username_query);
    if (mysqli_num_rows($check_username_result) > 0) {
        echo "<script>alert('This username already logged .please try again. Click OK to proceed to login.'); window.location.href = 'index.html';</script>";
        exit();
    }

    // Insert user data into database
    $insert_user_query = "INSERT INTO login (email, password) VALUES ('$email', '$password')";
    if (mysqli_query($conn, $insert_user_query)) {
        echo "<script>alert('Login successful. Click OK to proceed to login.'); window.location.href = 'multiple.html';</script>";
    } else {
        echo "Error: " . $insert_user_query . "<br>" . mysqli_error($conn);
    }

    mysqli_close($conn);
}
?>