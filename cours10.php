// https://kharroubihakim.xyz/cours10.php 

<?php
// Connexion à la base de données
require_once('config.php');
$conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

// Vérification de la connexion
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT valeur1, valeur2, date_heure FROM mes_donnees_cours10 ORDER BY date_heure DESC LIMIT 1";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Affichage des données
    $row = $result->fetch_assoc();
    echo "<h2>Dernières données reçues :</h2>";
    echo "<p><strong>Température :</strong> " . $row['valeur1'] . "°C</p>";
    echo "<p><strong>Humidité    :</strong> " . $row['valeur2'] . "%</p>";
    echo "<p><strong>Date et heure :</strong> " . $row['date_heure'] . "</p>";
} else {
    echo "Aucune donnée disponible.";
}


$conn->close();
?>
