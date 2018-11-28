package com.simplify.dataloader.servlet;

import java.net.URL;
import java.nio.charset.StandardCharsets;

import org.apache.commons.io.IOUtils;
import org.json.JSONException;
import org.json.JSONObject;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/csvreader")
public class MainServlet {

	@PostMapping(value = "/", produces = { MediaType.APPLICATION_JSON_VALUE })
	@ResponseBody
	public String requestProcessor(@RequestBody String value) throws JSONException {
		try {
			JSONObject json = new JSONObject(value);
			String urlPath = json.getJSONObject("requestData").getJSONArray("lookupDetails").getJSONObject(0)
					.getString("URL");
			System.out.println(urlPath);
			URL url = new URL(urlPath);
			String response = IOUtils.toString(url, StandardCharsets.UTF_8);
			return response;
		} catch (Exception e) {
			e.printStackTrace();
			return "Error in reading csv";
		}
	}
}
