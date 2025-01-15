#include <Stepper.h>
#include <Servo.h>

// Nombre de pas par tour du moteur 28BYJ-48 (2048 pas pour un tour complet)
#define STEPS 2048

// Définir les broches du moteur pour l'Arduino Mega
Stepper stepper(STEPS, 8, 10, 9, 11);
Stepper stepper2(STEPS, 4, 12, 5, 13);

// Définir la broche du bouton poussoir
const int buttonPin = 6;  // Broche du bouton poussoir
int buttonState = 0;       // Variable pour stocker l'état du bouton

// Définir la broche du servo moteur SG90
Servo lockServo;
const int servoPin = 3;  // Broche PWM pour le servo moteur

void setup() {
  // Initialiser le bouton comme entrée avec résistance Pull-up interne
  pinMode(buttonPin, INPUT_PULLUP);

  // Initialiser le servo moteur
  lockServo.attach(servoPin);  // Connecter le servo à la broche PWM

  // Initialiser la position du servo pour verrouiller la serrure (0°)
  lockServo.write(0);

  // Définir la vitesse du moteur
  stepper.setSpeed(15);  // Vitesse du moteur en tours par minute
  //stepper2.setSpeed(15);  // Vitesse du moteur en tours par minute
}

void loop() {
  // Lire l'état du bouton poussoir
  buttonState = digitalRead(buttonPin);

  // Si le bouton est appuyé (le bouton pousseur est connecté à GND, donc état LOW)
  if (buttonState == LOW) {
    // Déverrouiller la serrure (tourner le servo à 90°)
    lockServo.write(85);
    delay(1000);  // Attendre 1 seconde pour s'assurer que le servo est bien positionné

    // Ouvrir la porte (tourner le moteur de 90°)
    stepper.step(-STEPS / 4);
    //stepper2.step(-STEPS / 4);  // Effectuer un mouvement de 90° (1/4 de tour)
      // Effectuer un mouvement de -90° (1/4 de tour)
    delay(7000);  // Attendre 7 secondes (porte ouverte)
    
    // Fermer la porte (mouvement de -90°)
    stepper.step(STEPS / 4);  // Effectuer un mouvement de -90° (1/4 de tour dans l'autre sens)
    //stepper2.step(STEPS / 4);  // Effectuer un mouvement de 90° (1/4 de tour dans l'autre sens)
    delay(400);
    // Verrouiller la serrure (retourner le servo à 0°)
    lockServo.write(5);
  }
}
