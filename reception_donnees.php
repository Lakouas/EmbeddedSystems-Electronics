<?php
// Connexion à la base de données
require_once('config.php');
$conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

// Vérification de la connexion
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}



$valeur1 = isset($_GET['valeur1']) ? floatval($_GET['valeur1']) : null;
$valeur2 = isset($_GET['valeur2']) ? floatval($_GET['valeur2']) : null;


$sql = "INSERT INTO mes_donnees_cours10 (date_heure, valeur1, valeur2) VALUES (NOW(), '$valeur1', '$valeur2')";



if ($conn->query($sql) === TRUE) {
    echo "Données insérées avec succès";
} else {
    echo "Erreur lors de l'insertion des données: " . $conn->error;
}

$conn->close();
?>
