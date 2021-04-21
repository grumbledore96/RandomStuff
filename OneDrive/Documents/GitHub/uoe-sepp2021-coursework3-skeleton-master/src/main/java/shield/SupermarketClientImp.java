/**
 *
 */

package shield;

public class SupermarketClientImp implements SupermarketClient {
	  String name;
	  String status;
	  String postCode;
	  int orderNumber; 
	  String endpoint;
	  String CHI;
	  
  public SupermarketClientImp(String endpoint) {
	  this.endpoint = endpoint;
  }

  @Override
  public boolean registerSupermarket(String name, String postCode) {
	this.name = name;
	this.postCode = postCode;
	return true;
	//Needs to confirm that it connects to the server and updates them, and should return false there 
  }

  // **UPDATE2** ADDED METHOD
  @Override
  public boolean recordSupermarketOrder(String CHI, int orderNumber) {
	// Need to verify CHI with NHS
	this.CHI = CHI;
	if (isRegistered()) {
		this.orderNumber = orderNumber;
		return true;
	} else {
		System.out.println("The CHI given is false, recordSupermarketOrder failed.");
		return false;
	}
	

	//Needs to confirm that it connects to the server and updates them, and should return false there 
  }

  // **UPDATE**
  @Override
  public boolean updateOrderStatus(int orderNumber, String status) {
	this.orderNumber = orderNumber;
	this.status = status;
	return true;
	//Needs to confirm that it connects to the server and updates them, and should return false there 
  }

  @Override
  public boolean isRegistered() {
	// check with this.CHI that it's valid via the NHS and return true and false depending
    return false;
  }

  @Override
  public String getName() {
	 String returnValue = this.name;
	 return returnValue;
  }

  @Override
  public String getPostCode() {
	  String returnValue = this.postCode;
	  return returnValue;
  }
}
