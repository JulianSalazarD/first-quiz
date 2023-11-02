package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {

  private int quarter = 0;
  public static VendingMachine getInstance() {
    return new VendingMachineImpl();
  }

  @Override
  public void insertQuarter() {
    this.quarter += 25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {

    if(name.equals("ScottCola") && this.quarter < 75){
      throw new NotEnoughMoneyException();
    }

    if(name.equals("ScottCola")) {
      this.quarter -= 75;
      return new Drink() {
        @Override
        public String getName() {
          return "ScottCola";
        }
        @Override
        public boolean isFizzy() {
          return true;
        }
      };
    }
    if(name.equals("KarenTea") && this.quarter < 100){
      throw new NotEnoughMoneyException();
    }
    if(name.equals("KarenTea")) {
      this.quarter -= 100;
      return new Drink() {
        @Override
        public String getName() {
          return "KarenTea";
        }
        @Override
        public boolean isFizzy() {
          return false;
        }
      };
    }
      throw new UnknownDrinkException();
  }
}
