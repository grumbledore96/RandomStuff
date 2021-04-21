/**
 *
 */

package shield;

public class CateringCompanyClientImp implements CateringCompanyClient {
	  String name;
	  String status;
	  String postCode;
	  int orderNumber; 
	  String endpoint;

public CateringCompanyClientImp(String endpoint) {
	this.endpoint = endpoint;
	//assuming this should connect using the end point
  }

  @Override
  public boolean registerCateringCompany(String name, String postCode) {
	this.name = name;
	this.postCode = postCode;
	return true;
	//Needs to confirm that it connects to the server and updates them, and should return false there 
  }

  @Override
  public boolean updateOrderStatus(int orderNumber, String status) {
	this.orderNumber = orderNumber;
	this.status = status;
	return true;
	//Needs to confirm that it connects to the server and updates them, and should return false there 
  }

  @Override
  public boolean isRegistered() {
	  //Not sure what this does
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
