# Developed by @sandmaxprime

$headers=@{}
$headers.Add("accept", "application/json")
#Replace apikeyhere with your Virus Total Public or Enterprise APIKey
$headers.Add("x-apikey", "yourapikeyhere")

$vt_url = 'https://www.virustotal.com/api/v3/files'

$csv_path = 'C:\Users\Lionel\Desktop\IOCTest.csv'
$output_path = 'C:\Users\Lionel\Desktop\output.csv'

$hashes = Import-Csv -Path $csv_path | Select-Object -ExpandProperty Hash

write-output "Hash,MeaningfulName,Microsoft Malicious,Signature Type"

foreach ($hash in $hashes) {

    try
    {
        $query_url = "$vt_url/$hash"

        $response = Invoke-RestMethod -Uri $query_url -Method GET -Headers $headers -OutVariable GetStatusResponse
        write-output "$($hash),$($response.data.attributes.meaningful_name),$($response.data.attributes.last_analysis_results.Microsoft.category),$($response.data.attributes.last_analysis_results.Microsoft.result) "
        if ($response.data.attributes.last_analysis_results.Microsoft.category -ieq "undetected")
        {
            Write-Output "undetected hits: $($hash)" >> $output_path
        }
 
    }
    catch 
    {
        Write-Output "unsuccessful hits: $($hash)" >> $output_path
    }
}
