 #include <Stepper.h> // Include the header file

// change this to the number of steps on your motor
#define STEPS 32

// create an instance of the stepper class using the steps and pins
Stepper stepper1(STEPS, 8, 10, 9, 11);
Stepper stepper2(STEPS, 8, 10, 9, 11);

int Pval1 = 0;
int potVal1 = 0;
int Pval2 = 0;
int potVal2 = 0;

void setup() {
  Serial.begin(9600);
  stepper1.setSpeed(200);
  stepper2.setSpeed(200);
}

void loop() {

potVal1= map(analogRead(A0),0,1024,0,500);
potVal2= map(analogRead(A0),0,1024,0,500);
if (potVal1>Pval1)
  stepper1.step(5);
else if (potVal1<Pval1)
  stepper1.step(-5);
if (potVal2>Pval2)
  stepper1.step(5);
else if (potVal2<Pval2)
  stepper1.step(-5);
Pval1 = potVal1;
Pval2 = potVal2;

Serial.println(Pval1); //for debugging
}
