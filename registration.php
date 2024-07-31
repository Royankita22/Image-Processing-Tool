<?php
// Database connection
$host = 'localhost'; // Change this to your MySQL host
$dbname = 'ala'; // Change this to your database name
$username = 'username'; // Change this to your MySQL username
$password = 'password'; // Change this to your MySQL password

try {
    $conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Insert user data into database
	$name = $_POST['name'];
	$address = $_POST['address'];
	$email = $_POST['email'];
	$phoneno = $_POST['phoneno'];
    $password = $_POST['password'];

    $stmt = $conn->prepare("INSERT INTO registration (name, address, email, password, phoneno) VALUES (:name, :address, :email, :password, :phoneno)");
    $stmt->bindParam(':name', $name);
	$stmt->bindParam(':address', $address);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':password', $password);
	$stmt->bindParam(':phoneno', $phoneno);
    $stmt->execute();
	// Redirect to the login page
    echo "<script>alert('Registration successful. Click OK to proceed to login.'); window.location.href = 'index.html';</script>";
    exit; // Ensure that no further code is executed after the redirection
} catch(PDOException $e) {
    echo "Error: " . $e->getMessage();
}
?>
