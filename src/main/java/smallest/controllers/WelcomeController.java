package smallest.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class WelcomeController {
	
	@RequestMapping(method = RequestMethod.GET, produces = {"application/json"}, value = "/app")
	public @ResponseBody String helloWorld() {
		
		//Flux
		
		
		
		
		return "Hello World 0.0.2!!!"; //"application/json" mean this is a text not a redirect
	}
}
